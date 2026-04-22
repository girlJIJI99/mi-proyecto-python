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
#Consolidado con IA 
#El uso de keys, choice y list
# Se necesita que la computadora elija un Pokémon automáticamente y sin intervención del usuario. 
# Como los Pokémon están guardados en un diccionario, primero se utiliza keys() para obtener los nombres disponibles, 
# luego list() para poder manejarlos como una lista, y finalmente random.choice() para seleccionar uno al azar.

else: 
    print ("La computadora esta eligiendo...")
    opcion2 = random.choice(list(CATALOGO_POKEMON.keys())) # En tu código, keys(), list() y random.choice() trabajan juntos para que la computadora elija un Pokémon al azar
    jugador2 = crear_pokemon(opcion2)
    print(f"La computadora ha elegido al jugado {jugador2.nombre}")
#------------------------------------------------------------  

# ====BATALLA====
print("\n Comienza la batalla!!")
print(f"{jugador1.nombre} VS {jugador2.nombre}")


turno_jugador1 = True
while jugador1.hp_actual > 0  and jugador2.hp_actual > 0:


    if turno_jugador1:
        actual = jugador1
        oponente = jugador2
        nombre_turno = "Jugador1"
    else:
        actual = jugador2
        oponente= jugador1
        nombre_turno = "jugador2" if modo == "1" else "Computadora"

print("\n" + "-" * 40)
print(f"Turno de: {actual.nombre} ({nombre_turno})")
print(f"[HP: {actual.hp_actual}]-- [EP: {actual.energia_actual}]")



#---------------------------TURNO DEL JUGADOR ----------------------------












