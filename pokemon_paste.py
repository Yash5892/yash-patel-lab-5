import sys
from pastebin_api import create_paste
from poke_api import get_pokemon_info

def get_pokemon_name():
    """
    Gets the Pokémon name from the command line parameter.

    Returns:
    str: The Pokémon name input as a command line parameter.
    """
    if len(sys.argv) < 2:
        print("Error: No Pokémon name provided.")
        sys.exit(1)
    return sys.argv[1]

def construct_paste_content(pokemon_info):
    """
    Constructs the title and body text for the new paste.

    Parameters:
    pokemon_info (dict): Dictionary of Pokémon information.

    Returns:
    tuple: The paste title and body text as strings.
    """
    name = pokemon_info['name'].capitalize()
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    title = f"{name}'s Abilities"
    body_text = "\n".join(f"- {ability}" for ability in abilities)
    return title, body_text

def main():
    pokemon_name = get_pokemon_name()
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        title, body_text = construct_paste_content(pokemon_info)
        paste_url = post_new_paste(title, body_text, expiration='1M', public=False)
        if paste_url:
            print(f"Paste URL: {paste_url}")
        else:
            print("Failed to create paste.")
    else:
        print("Failed to fetch Pokémon information.")

if __name__ == "__main__":
    main()