from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_clases import *
import random


def crear_pokemon(datos):
    tipo = datos ["tipo"]
    if tipo == "Fuego":
        return PokemonFuego(datos["nombre"], datos["hp"], datos["ep"])
    elif tipo == "Agua":
        return PokemonAgua(datos ["nombre"], datos ["hp"], datos["ep"])
    elif tipo =="Planta":
        return PokemonPlanta (datos["nombre", datos["hp"], datos ["ep"]])
    elif tipo =="Electrico":
        return PokemonElectrico(datos["nombre"], datos["hp"], datos["ep"])

#============================= MENU===============================
print("=" * 50)
print(" SIMULADOR DE BATALLAS POKEMON")
print("=" * 50)
 

print("1. Jugador VS Jugador")
print("2. Jugador VS Computadora")

while True: 
    modo = input("Seleccione modo: ") 
    if modo == "1" or modo == "2": 
        break 
    else: 
        print("Opción inválida, intenta de nuevo.")


#ELEGIR POKEMON CON VALIDACION
#=====JUGADOR 1=======
while True:
    opcion1 = input("jugador 1, elige tu Pokemon:")
    if opcion1 in CATALOGO_POKEMON:
        jugador1 = crear_pokemon(opcion1)
        print(f"Has seleccionado{jugador1.nombre}")
        break
    else:
        print("opcion invalida.")

#===== COMPUTADORA o jugador 2====
if modo == "1":
    while True:
        opcion2 = input("Jugador 2, elige tu pokemon:")
        if opcion2 in CATALOGO_POKEMON:
            jugador2 = crear_pokemon(opcion2)
        else:
            print("Opcion invalida")
#------------------------------------------------------------   
else: 
    print ("La computadora esta eligiendo...")
    opcion2 = random.choice(list(CATALOGO_POKEMON.keys()))
    jugador2 = crear_pokemon(opcion2)
    print(f"La computadora ha elegido al jugado {jugador2.nombre}")
#------------------------------------------------------------  

# ====BATALLA====
print("\n Comienza la batalla!!")
print(f"{jugador1.nombre} VS {jugador2.nombre}")


turno_jugador1 = True
while jugador1.hp_actual > 0  and jugador2.hp_actual > 0:











