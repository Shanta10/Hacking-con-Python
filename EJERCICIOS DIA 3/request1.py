import requests

def get_pokemon_info(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon"
    try:
        response = requests.get(url)
        response.raise_for_status()
        pokemon_data = response.json()
        abilities = [ability['ability']['name'].capitalize() for ability in pokemon_data['abilities']]
        types = [type_entry['type']['name'].capitalize() for type_entry in pokemon_data['types']]
        return pokemon_data['name'].capitalize(), abilities, types
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None, None, None
    except KeyError as e:
        print(f"Error al procesar los datos recibidos: {e}")
        return None, None, None

def save_to_file(pokemon_name, abilities, types):
    filename = f"{pokemon_name}.txt"
    with open(filename, 'w') as file:
        file.write(f"Nombre: {pokemon_name}\n")
        file.write("Habilidades:\n")
        for ability in abilities:
            file.write(f"- {ability}\n")
        file.write("Tipos:\n")
        for pokemon_type in types:
            file.write(f"- {pokemon_type}\n")
    print(f"Resultados guardados en '{filename}'.")

def main():
    pokemon_name = input("Ingrese el nombre de un Pokémon: ")
    pokemon_name, abilities, types = get_pokemon_info(pokemon_name)
    if pokemon_name:
        print(f"Nombre: {pokemon_name}")
        print("Habilidades:")
        for ability in abilities:
            print(f"- {ability}")
        print("Tipos:")
        for pokemon_type in types:
            print(f"- {pokemon_type}")
        save_option = input("¿Desea guardar los resultados en un archivo? (s/n): ")
        if save_option.lower() == 's':
            save_to_file(pokemon_name, abilities, types)

if __name__ == "__main__":
    main()
