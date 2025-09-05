from random import randint, random

class Trabajo:                          # Clase Celda
    __tiempo: int
    __hojas: int
    __sig: int

    def __init__(self, tiempo, hojas):
        self.__tiempo = tiempo
        self.__hojas = hojas
        self.__sig = None

    def getTiempo(self):
        return self.__tiempo
    
    def setTiempo(self, tiempo):
        self.__tiempo = tiempo

    def getHojas(self):
        return self.__hojas
    
    def setHojas(self, hojas):
        self.__hojas = hojas

    def getSiguiente(self):
        return self.__sig
    
    def setSiguiente(self, sig):
        self.__sig = sig

class ColaEncadenada:
    __primero: object
    __ultimo: object
    __cant: int

    def __init___(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def longitud(self):
        return self.__cant
    
    def insertar(self, tiempo, hojas):
        nuevo = Trabajo(tiempo, hojas)

        if self.vacia():
            self.__primero = nuevo
        else:
            self.__ultimo.setSiguiente(nuevo)

        self.__ultimo = nuevo
        self.__cant += 1
    
    def surpimir(self):
        if self.vacia():
            print("Cola vacía")
            return None
        
        else:
            tiempoEliminado = self.__primero.getTiempo()    # Equivalente a elemento = actual.getItem() 
            hojasEliminadas = self.__primero.getHojas()
            self.__cant -= 1
            self.__primero = self.__primero.getSiguiente()
            return tiempoEliminado, hojasEliminadas

    def recuperar(self):
        return self.__primero
    
    def recorrer(self):
        if actual is None:
            actual = self.__primero

        while actual != None:
            print(actual.getTiempo(), actual.getHojas())
            actual = actual.getSiguiente()

def simuladorImpresora(tiempoSimulacion, tiempoLlegada, cola):
    reloj = 0
    trabajosImpresos = 0
    impresora = 0
    tiempoAtencionTotal = 0

    while reloj < tiempoSimulacion:
        if random() <= tiempoLlegada:
            hojas = randint(1, 100)
            cola.insertar(reloj, hojas)
            