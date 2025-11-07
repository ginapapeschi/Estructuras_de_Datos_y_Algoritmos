import numpy as np

class ListaSecuencial:
    pass

class TablaHash:
    __tamaño: int
    __tabla: np.array
    __overflow: np.array
    
    def __init__(self, tamañoTabla, tamañoBucket, factorCarga=0.7):
        self.__tamaño = self.obtenerPrimo(round(tamañoTabla/factorCarga))
        self.__tabla = np.empty(self.__tamaño, dtype=object)
        for i in range(self.__tamaño):
            self.__tabla[i] = ListaSecuencial(tamañoBucket)
        self.__overflow = ListaSecuencial(round (tamañoBucket * 0.2))

    def hashing(self, valor):
        return valor % self.__tamaño

    def insertar(self, valor):
        indice = self.hashing(valor)
        if not self.__tabla[indice].llena():
            self.__tabla[indice].insertarPorContenido(valor)
        else:
            self.__overflow.insertarPorContenido(valor)

    def busqueda(self, valor):
        indice = self.hashing(valor)
        encontrado = False
        if self.__tabla[indice].busquedaBinaria(valor):
            encontrado = True
        elif self.__overflow.busquedaBinaria(valor):
            encontrado = True
        return encontrado