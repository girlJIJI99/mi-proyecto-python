#Clae base abstracta
from abc import ABC, abstractmethod
import random

class Pokemon(ABC):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.nombre = nombre
        self.__hp_actual  = hp_maximo 
        self.__energia_actual = energia_maxima
        self.energia_maxima = energia_maxima
        self.defendiendo = False


#Encapsulamiento  uso de decorador "@property"
    @property
    def hp_actual(self):
        return self.__hp_actual
    #Settter no permite negativos 

    @hp_actual.setter
    def hp_actual(self, valor):
        if valor < 0:
            self.__hp_actual = 0
        else:
            self.__hp_actual = valor
    @property
    def energia_actual(self):
        return self.__energia_actual

    @energia_actual.setter
    def energia_actual(self, valor):
        if valor < 0:
            self.__energia_actual = 0
        elif valor > self.energia_maxima:
            self.__energia_actual = self.energia_maxima
        else:
            self.__energia_actual = valor

    def defender(self):
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.defendiendo = True
            print(f"{self.nombre} se está defendiendo")
        else:
            print("No tienes  energía suficiente" )

    def descansar(self):
        self.energia_actual += 20
        print(f"{self.nombre}   recupera energía" )
    
    @abstractmethod
    def atacar(self, oponente):
        pass

# 4 CLASES HIJAS esenciales que heredan de la clase base "POKEMON"
#CLASE AGUA CON ISINSTANCE
class PokemonAgua(Pokemon):
    def atacar(self, oponente):
        #Validacion principal 
        if self.energia_actual <15:
            print("No cuenta con energia suficente.")
            return
        self.energia_actual -= 15
        daño = 10
#--------------- Segunda y tercera Validacion
        if isinstance(oponente, PokemonFuego):
            daño *= 2
            print("Es super efectivo.")
        if oponente.defendiendo:
            daño //= 2
            oponente.defendiendo = False
        oponente.hp_actual -= daño
        print(f"{self.nombre} hace {daño} de daño")


#CALSE FUEGO CON INSINSTANCE
class PokemonFuego(Pokemon):
    def atacar (self, oponente):
        if self.energia_actual <15:
            print("No tiene energia sufciente")
            return
        self.energia_actual -=15
        daño = 10
#---------------Segunda y tercera Validacion
        if isinstance(oponente, PokemonPlanta):
            daño *= 2
            print("Es super efectivo.")
        if oponente.defendiendo:
            daño //= 2
            oponente.defendiendo = False
        oponente.hp_actual -= daño
        print(f"{self.nombre} hace {daño} de daño")

#CLASE PLANTA CON INSINSTANCE

class PokemonPlanta(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual <15:
            print("No tiene energia suficiente")
            return
        self.energia_actual -= 15
        daño = 10 
#---------------Segunda y tercera Validacion
        if isinstance(oponente, PokemonAgua):
            daño *= 2
            print("Es super efectivo.")
        if oponente.defendiendo:
            daño //= 2
            oponente.defendiendo = False

        oponente.hp_actual -= daño
        print(f"{self.nombre} hace {daño} de daño")

#CLASE POKEMON ELECTRICO(POKEMON):
class PokemonElectrico(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual<15:
            print("No tiene energia suficiente")
            return
        self.energia_actual -= 15
        daño =10

#--------------Segunda y tercera validacion

        if  random.random() <0.2:
            print("El oponente quedo paralizado.")
            oponente.paralizado = True 
        if oponente.defendiendo:
            daño//=2
            oponente.defendiendo = False

            oponente.hp_actual -= daño
            print(f"{self.nombre} hace {daño} de daño")





