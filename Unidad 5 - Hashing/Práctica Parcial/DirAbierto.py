import numpy as np

class TablaHash:
    __tamaño: int
    __tabla: np.ndarray

    def __init__(self, tamaño, factorCarga=0.7):
        self.__tamaño = self.obtenerPrimo(round(tamaño/factorCarga))
        self.__tabla = np.full(self.__tamaño, None, dtype=object)

    def esPrimo(self, tamaño):
        esPrimo = True
        if tamaño < 2:
            esPrimo = False
        else:
            i = 2
            while i <= int(tamaño ** 0.5) and esPrimo:
                if tamaño % i == 0:
                    esPrimo = False
                i += 1
        return esPrimo
    
    def obtenerPrimo(self, tamaño):
        if self.esPrimo(tamaño):
            resultado = tamaño
        else:
            siguiente = tamaño + 1
            while not self.esPrimo(siguiente):
                siguiente += 1
            resultado = siguiente
        return resultado
    
    def hashing(self, valor):
        return valor % self.__tamaño
    
    def insertar(self, valor):
        indice = self.hashing(valor)
        inicio = indice
        repetido = False
        tablaLlena = False
        while self.__tabla[indice] is not None and not repetido and not tablaLlena:
            if self.__tabla[indice] == valor:
                repetido = True
            else:
                indice = (indice + 1) % self.__tamaño
                if indice == inicio:
                    tablaLlena = True
        if repetido:
            print("Valor en tabla") 
        elif tablaLlena:
            print("Tabla llena")
        else:
            self.__tabla[indice] = valor

    def buscar(self, valor):
        indice = self.hashing(valor)
        inicio = indice
        encontrado = False
        tablaLlena = False
        while self.__tabla[indice] is not None and encontrado and not tablaLlena:
            if self.__tabla[indice] == valor:
                encontrado = True
            else:
                indice = (indice + 1) % self.__tamaño
            if indice == inicio:
                tablaLlena = True
        return encontrado