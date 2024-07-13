import requests
import sys

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'YVndm5puZcbr-N3sNFK18AAnb8RDKdv7'

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter
    clean_name = pokemon_name.strip()
    poke_name = clean_name.lower()

    # Build a clean URL and use it to send a GET request
    resp = requests.get(POKE_API_URL + poke_name)

    # If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if resp.status_code == requests.codes.ok:
        return resp.json()
    else:
        print(f"Failed to get information for {poke_name}. HTTP Status code: {resp.status_code}")
        return None

def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 

    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    params = {
        "api_dev_key": API_DEV_KEY,
        "api_option": "paste",
        "api_paste_code": body_text,
        "api_paste_name": title,
        "api_paste_expire_date": expiration,
        "api_paste_private": 0 if listed else 1 
    }

    resp = requests.post(PASTEBIN_API_POST_URL, data=params)

    if resp.status_code == requests.codes.ok:
        return resp.text
    else:
        print("Failed to create a new paste")
        print(f"{resp.status_code} {resp.reason} {resp.text}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <pokemon_name>")
        sys.exit(1)

    pokemon_name = sys.argv[1]
    poke_info = get_pokemon_info(pokemon_name)

    if poke_info:
        abilities = [ability['ability']['name'] for ability in poke_info['abilities']]
        abilities_list = "\n".join(f"- {ability}" for ability in abilities)

        title = f"{pokemon_name.capitalize()}'s Abilities"
        paste_url = post_new_paste(title, abilities_list)

        if paste_url:
            print(f"Paste created successfully! You can view it here: {paste_url}")
        else:
            print("Failed to create paste.")
    else:
        print("Could not get Pokémon information.")

if __name__ == '__main__':
    main()
