from pokedex import pokedex
from pokemon_clases import *
import random


def mostrar_pokedex():
    for clave, datos in pokedex.items():
        print(f"[{clave}] {datos['nombre']} | Tipo: {datos['tipo']} | HP: {datos['hp_maximo']} | EP: {datos['energia_maxima']}")


def crear_pokemon(opcion):
    datos = pokedex[opcion]

    if datos["tipo"] == "Fuego":
        return PokemonFuego(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])
    elif datos["tipo"] == "Agua":
        return PokemonAgua(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])
    elif datos["tipo"] == "Planta":
        return PokemonPlanta(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])
    elif datos["tipo"] == "Electrico":
        return PokemonElectrico(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])


def turno(jugador, oponente):
    if jugador.paralizado:
        print(f"{jugador.nombre} está paralizado y pierde turno")
        jugador.paralizado = False
        return

    print(f"\nTURNO DE {jugador.nombre}")
    print(f"HP: {jugador.hp_actual}/{jugador.hp_maximo} | EP: {jugador.energia_actual}/{jugador.energia_maxima}")

    while True:
        try:
            opcion = int(input("1.Atacar 2.Defender 3.Descansar: "))
            break
        except ValueError:
            print("Entrada inválida")

    if opcion == 1:
        jugador.atacar(oponente)
    elif opcion == 2:
        jugador.defender()
    elif opcion == 3:
        jugador.descansar()


def turno_cpu(cpu, jugador):
    accion = random.randint(1, 3)
    print(f"\nCPU elige {accion}")

    if accion == 1:
        cpu.atacar(jugador)
    elif accion == 2:
        cpu.defender()
    else:
        cpu.descansar()


def batalla(p1, p2, cpu=False):
    while p1.hp_actual > 0 and p2.hp_actual > 0:
        turno(p1, p2)

        if p2.hp_actual <= 0:
            break

        if cpu:
            turno_cpu(p2, p1)
        else:
            turno(p2, p1)

    print("\nFIN DE LA BATALLA")
    if p1.hp_actual > 0:
        print(f"Gana {p1.nombre}")
    else:
        print(f"Gana {p2.nombre}")


# MAIN
print("1. PvP\n2. PvE")

modo = int(input("Modo: "))

mostrar_pokedex()

op1 = int(input("Jugador 1 elige: "))
p1 = crear_pokemon(op1)

if modo == 1:
    op2 = int(input("Jugador 2 elige: "))
    p2 = crear_pokemon(op2)
    batalla(p1, p2)
else:
    op2 = random.choice(list(pokedex.keys()))
    p2 = crear_pokemon(op2)
    batalla(p1, p2, cpu=True)