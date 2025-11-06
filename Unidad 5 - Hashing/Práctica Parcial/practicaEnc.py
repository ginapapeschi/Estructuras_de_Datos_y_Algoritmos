import numpy as np

class ListaEncadenada:
    pass

class TablaHash:
    __tamaño: int
    __tabla: np.array

    def __init__(self, tamaño, factorCarga=0.7):
        self.__tamaño = self.obtenerPrimo(round(tamaño/factorCarga))
        self.__tabla = np.empty(self.__tamaño, dtype=object)
        for i in range(self.__tamaño):
            self.__tabla[i] = ListaEncadenada()
    
    def hashing(self, valor):
        return valor % self.__tamaño
    
    def insertar(self, valor):
        indice = self.hashing(valor)
        self.__tabla[indice].insertar(valor)

    def buscar(self, valor):
        indice = self.hashing(valor)
        actual = self.__tabla[indice].getCabeza()
        encontrado = False
        while actual != None and actual.getValor() != valor:
            actual = actual.getSiguiente()
        if actual:
            encontrado = True
        return encontrado
    