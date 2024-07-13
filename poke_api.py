'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    clean_name=pokemon_name.strip(' ')
    poke_name=clean_name.lower()

    # TODO: Build a clean URL and use it to send a GET request
    resp=requests.get(POKE_API_URL+poke_name)

    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if resp.status_code==requests.codes.ok:
        print(f"Obtaining the information for {poke_name} was a success.")
        return resp.json()
    # TODO: If the GET request failed, print the error reason and return None
    else:
        return None

if __name__ == '__main__':
    main()