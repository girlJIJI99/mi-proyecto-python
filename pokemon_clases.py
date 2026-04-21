#Clae base abstracta
class Pokemon:
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
            print("No tienes energía suficiente")

    def descansar(self):
        self.energia_actual += 20
        print(f"{self.nombre} recupera energía")