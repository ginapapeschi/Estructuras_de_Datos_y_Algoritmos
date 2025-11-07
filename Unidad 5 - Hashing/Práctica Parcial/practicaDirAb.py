import numpy as np

class TablaHash:
    __tamaño: int
    __tabla: np.ndarray
    
    def __init__(self, tamaño, factorCarga=0.7):
        self.__tamaño = self.obtenerPrimo(round(tamaño/factorCarga))
        self.__tabla = np.full(self.__tamaño, None, dtype=object)
    
    def hashing(self, valor):
        return valor % self.__tamaño
    
    def insertar(self, valor):
        indice = self.hashing(valor)
        inicio = indice
        repetido = False
        tablaLlena = False
        while self.__tabla[indice] != None and not repetido and not tablaLlena:
            if self.__tabla[indice] == valor:
                repetido = True
            else:
                indice = (indice + 1) % self.__tamaño
                if indice == inicio:
                    tablaLlena = True
        if repetido:
            print("Repetido")
        elif tablaLlena:
            print("Tabla llena")
        else:
            self.__tabla[indice] = valor

    def buscar(self, valor):
        indice = self.hashing(valor)
        inicio = indice
        encontrado = False
        tablaLlena = False
        while self.__tabla[indice] != None and not encontrado and not tablaLlena:
            if self.__tabla[indice] == valor:
                encontrado = True
            else:
                indice = (indice + 1) % self.__tamaño
                if indice == inicio:
                    tablaLlena = True
        return encontrado
    
