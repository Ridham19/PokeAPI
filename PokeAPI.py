import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Got the Data")
        print("<-------------------------------------------->")
        pokemon_data = response.json()
        return pokemon_data
    elif response.status_code == 404:
        print("<---Not Found--->")
    else:
        print(f"failed to get data of {name}")
        print(response.status_code)


pokemon = input("Enter pokemon name: ").lower()
pokemon_data = get_pokemon_info(pokemon)

try:
    print(f"name: {pokemon_data['name']}")
    print(f"ID: {pokemon_data['id']}")
    print(f"type: {pokemon_data['types'][0]['type']['name']}")
    print(f"ability 1: {pokemon_data['abilities'][0]['ability']['name']}")
    try:
        print(f"ability 2: {pokemon_data['abilities'][1]['ability']['name']}")
    except IndexError:
        pass
    try:
        print(f"ability 3: {pokemon_data['abilities'][2]['ability']['name']}")
    except IndexError:
        pass
    print(f"Height: {pokemon_data['height']} units")
    print(f"weight: {pokemon_data['weight']} units")
except TypeError:
    print("Maybe there is error in Name!")
