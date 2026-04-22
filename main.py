from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_clases import *
import random
# ============================== 
# # FUNCIÓN PARA CREAR POKÉMON 
# # ==============================

def crear_pokemon(clave):
    datos = CATALOGO_POKEMON[clave]  

    tipo = datos["tipo"]
    if tipo == "Fuego":
        return PokemonFuego(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])

    elif tipo == "Agua":
        return PokemonAgua(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])

    elif tipo == "Planta":
        return PokemonPlanta(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])

    elif tipo == "Electrico":
        return PokemonElectrico(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])
#============================= MENU===============================
print("=" * 50)
print("================================")
print("SIMULADOR DE BATALLAS POKEMON")
print("================================")
print("=" * 50)
 

print("1. Jugador VS Jugador")
print("2. Jugador VS Computadora")

while True: 
    modo = input("Seleccione modo: ") 
    if modo == "1" or modo == "2": 
        break 
    else: 
        print("Opción inválida, intenta de nuevo.")


# ELEGIR POKEMON CON VALIDACION
# ===== JUGADOR 1 =======
mostrar_catalogo_disponible()
print("====== CATÁLOGO OFICIAL POKÉMON ========")

while True:
    opcion1 = input("Jugador 1, elige tu Pokémon: ").strip()

    if opcion1 in CATALOGO_POKEMON:
        jugador1 = crear_pokemon(opcion1)
        print(f"Has seleccionado a {jugador1.nombre}!")
        break
    else:
        print("Opción inválida.")

#===== COMPUTADORA o jugador 2====
if modo == "1":
    while True:
        opcion2 = input("Jugador 2, elige tu pokemon:")
        if opcion2 in CATALOGO_POKEMON:
            jugador2 = crear_pokemon(opcion2)
            break
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

#------------ACCIONES--------------------------

turno_jugador1 = True
while jugador1.hp_actual > 0  and jugador2.hp_actual > 0:
    


    if turno_jugador1:
        actual = jugador1
        oponente = jugador2
        nombre_turno = "Jugador 1"
    else:
        actual = jugador2
        oponente= jugador1
        nombre_turno = "jugador 2" if modo == "1" else "Computadora"

    print("\n" + "-" * 50)
    print(f"Turno de: {actual.nombre} ({nombre_turno})")
    print(f"[HP: {actual.hp_actual}]-- [EP: {actual.energia_actual}]")



# --------------------------- ACCIÓN ----------------------------
    if modo == "1" or turno_jugador1:

        print("¿Qué acción deseas realizar?")
        print("1. Atacar")
        print("2. Defender")
        print("3. Descansar")

    while True:
        accion = input("> Opción: ")
        if accion in ("1", "2", "3"):
            break
        else:
            print("Opción inválida")

else:
    accion = random.choice(["1", "2", "3"])
    acciones = {"1": "Atacar", "2": "Defender", "3": "Descansar"}
    print(f"La computadora elige: {accion} ")



# --------------------------- EJECUTAR ----------------------------
    if accion == "1":
        actual.atacar(oponente)
    elif accion == "2":
        actual.defender()
    elif accion == "3":
        actual.descansar()


# --------------------------- CAMBIAR TURNO ----------------------------
    turno_jugador1 = not turno_jugador1
# ============================== # RESULTADO # ============================== 
print("\n" + "=" * 50) 
if jugador1.hp_actual > 0: 
    print(f"{jugador1.nombre} ha ganado la batalla ") 
else: 
    print(f"{jugador2.nombre} ha ganado la batalla ") 
print("=" * 50)