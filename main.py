# main.py
from fuego import PokemonFuego
from agua import PokemonAgua
from pokemonM import PokemonConHabilidad


def main():
    # Crear instancias de las clases hijo directas
    charizard = PokemonFuego("Charizard", 36, 1200)  # Clase hijo de PokemonTipo, y aqui solo le pones al final el tipo que quieres, y haces eso en todos los demas
    squirtle = PokemonAgua("Squirtle", 5, 30)  # Clase hijo de PokemonTipo
    zapdos_con_habilidad = PokemonConHabilidad("Zapdos", 50, 5000, "Electrocañón")  # Clase hijo de PokemonElectrico

    # Mostrar información y ataques
    print(charizard)
    print(charizard.atacar())
    print()

    print(squirtle)
    print(squirtle.atacar())
    print()

    print(zapdos_con_habilidad)
    print(zapdos_con_habilidad.atacar())


if __name__ == "__main__":
    main()
