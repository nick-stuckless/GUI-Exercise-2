'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests
import image_lib
import os

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_into() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    print(get_pokemon_names())
    return

def get_pokemon_info(pokemon):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter by:
    # - Converting to a string object,
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon = str(pokemon).strip().lower()

    # Check if Pokemon name is an empty string
    if pokemon == '':
        print('Error: No Pokemon name specified.')
        return

    # Send GET request for Pokemon info
    print(f'Getting information for {pokemon.capitalize()}...', end='')
    url = POKE_API_URL + pokemon
    resp_msg = requests.get(url)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')

    # TODO: Define function that gets a list of all Pokemon names from the PokeAPI
def get_pokemon_names():
    print("Getting list of pokemon names...", end='')

    params = {
        "limit": 2000,
        "offset":0,
    }
    respo = requests.get(POKE_API_URL, params=params)

    if respo.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        poke_dict =  respo.json()
        return [p["name"] for p in poke_dict["results"]]
    else:
        print('failure')
        print(f'Response code: {respo.status_code} ({respo.reason})')

    
    return

    # TODO: Define function that downloads and saves Pokemon artwork
def get_pokemon_art(pokemon, image_dir):
    poke_info = get_pokemon_info(pokemon)
    if not poke_info:
        return
    
    art_url = poke_info["sprites"]["other"]["official-artwork"]["front_default"]
    if not art_url:
        print(f"No artwork found for {pokemon}")
        return
    
    file_ext = art_url.split(".")[-1]
    path = os.path.join(image_dir, f"{pokemon}.{file_ext}")
    if os.path.isfile(path):
        print(f"{pokemon}'s artwork already exists")
        return path


    image = image_lib.download_image(art_url)
    if not image:
        return
    
    #file_ext = art_url.split(".")[-1]
    #path = os.path.join(image_dir, f"{pokemon}.{file_ext}")
    if image_lib.save_image_file(image, path):
        return path

    return

if __name__ == '__main__':
    main()