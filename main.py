from agua import PokemonAgua
from planta import PokemonPlanta
from charizard import Charizard

def main():
    squirtle = PokemonAgua("Squirtle", 10)
    bulbasaur = PokemonPlanta("Bulbasaur", 10)
    charizard = Charizard("Charizard",50)

    pokemons = [squirtle, bulbasaur, charizard]

    for pokemon in pokemons:
        print(pokemon.mostrar_info())
        print(pokemon.ataque_elemental())

        if isinstance(pokemon, PokemonAgua):
            print(pokemon.hidrobomba())

        if isinstance(pokemon, PokemonPlanta):
            print(pokemon.rayo_solar())

        if isinstance(pokemon, Charizard):
            print(pokemon.ataque_aereo())
            print(f"Tipo secundario: {pokemon.get_tipo_secundario()}")

        print("---")

if __name__ == "__main__":
    main()