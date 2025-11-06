import numpy as np

class Nodo:
    __elemento: object
    __sig: object

    def __init__(self, elemento):
        self.__elemento = elemento
        self.__sig = None
    
    def getElemento(self):
        return self.__elemento
    
    def setElemento(self, elemento):
        self.__elemento = elemento
    
    def getSiguiente(self):
        return self.__sig
    
    def setSiguiente(self, sig):
        self.__sig = sig

class ListaEnlazada:
    __cabeza: Nodo

    def __init__(self):
        self.__cabeza = None

    def getCabeza(self):
        return self.__cabeza
    
    def __str__(self):
        actual = self.__cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.getElemento()))
            actual = actual.getSiguiente()
        return " -> ".join(elementos)

    def insertar(self, elemento):
        nuevo = Nodo(elemento)
        actual = self.__cabeza
        repetido = False # Evita insertar duplicados.

        if not actual: # Si la lista está vacía.
            self.__cabeza = nuevo
        else:
            while actual.getSiguiente() != None: # Mientras haya un siguiente nodo al actual.
                # Se corta antes de entrar al último nodo.
                if actual.getElemento() == elemento: # Si está repetido.
                    repetido = True
                actual = actual.getSiguiente()
            if actual.getElemento() == elemento: # Revisa el último nodo de la lista.
                repetido = True
            
            if not repetido: # Si no está en la lista lo inserta al final.
                actual.setSiguiente(nuevo)

class TablaHash:
    __tamaño: int
    __tabla: np.array

    def __init__(self, tamaño, factorCarga=0.7):
        self.__tamaño = self.obtenerPrimo(round(tamaño/factorCarga))
        self.__tabla = np.empty(self.__tamaño, dtype=object)
        for i in range(self.__tamaño):
            self.__tabla[i] = ListaEnlazada()
    
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
            while not self.esPrimo():
                siguiente += 1
            resultado = siguiente
        return resultado
    
    def hashing(self, valor):
        return valor % self.__tamaño
    
    def hashingAlfanumerico(self, cadena):
        indice = 0
        base = 31
        for letra in cadena:
            indice = (indice * base + ord(letra)) % self.__tamaño
        return indice
    
    def insertar(self, valor):
        indice = self.hashing(valor)
        self.__tabla[indice].insertar(valor)

    def buscar(self, valor):
        indice = self.hashing(valor)
        actual = self.__tabla[indice].getCabeza()
        encontrado = False
        while actual != None and actual.getElemento() != valor:
            actual = actual.getSiguiente()
        if actual:
            encontrado = True
        return encontrado
    
    