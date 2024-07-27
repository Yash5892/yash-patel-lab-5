import requests

def get_pokemon_info(pokemon_name):
    """
    Fetches information for a specified Pokémon from the PokéAPI.

    Parameters:
    pokemon_name (str): The name or PokéDex number of the Pokémon.

    Returns:
    dict: Dictionary containing Pokémon information if successful, None otherwise.
    """
    pokemon_name = str(pokemon_name).strip().lower()
    print(f"Getting information for {pokemon_name}...")

    url = f"https://pokeapi.co/api/v2/pokemon/1/{pokemon_name}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Information fetched successfully.")
        return response.json()
    else:
        print(f"Failed to fetch information. Response code: {response.status_code}")
        return None

# Test the function
if __name__ == "__main__":
    info = get_pokemon_info("pikachu")
    print(info)