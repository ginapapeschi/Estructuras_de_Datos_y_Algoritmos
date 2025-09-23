import numpy as np

class PilaSecuencial:
    __tope: int
    __max: int
    __cant: int
    __items: np.ndarray

    def __init__(self, max):
        self.__tope = -1
        self.__max = max
        self.__cant = 0
        self.__items = np.empty(max, dtype=object)

    def getTope(self):
        return self.__tope
    
    def getCantidad(self):
        return self.__cant
    
    def llena(self):
        return self.__cant == self.__max

    def vacia(self):
        return self.__tope == -1
    
    def insertar(self, elemento):
        if self.llena():
            print("Pila llena")

        else:
            self.__tope += 1
            self.__items[self.__tope] = elemento
            self.__cant += 1
            #print(f"Elemento {elemento} insertado en la posición {self.__tope}")

    def suprimir(self):
        if self.vacia():
            print("Pila vacía")

        else:
            borrado = self.__items[self.__tope]
            self.__tope -= 1
            self.__cant -= 1
            return borrado
        
    def mostrar(self):
        if not self.vacia():
            print("\nContenido de la pila:")
            for i in range(self.__cant - 1, -1, -1): # Recorre desde el tope hacia abajo, naturalmente LIFO.
                print(f"[{i}] -> {self.__items[i]}")
        
        else:
            print("Pila vacía")

def calcularPeldaños(pila):
    c = 0
    n = int(input("Ingrese la cantidad de peldaños: "))
    pila.insertar((n, [])) # n son los peldaños RESTANTES por subir, la lista [] es la secuencia actual de pasos.

    while not pila.vacia():
        restante, secuencia = pila.suprimir() # Devuelve la última tupla en la pila.

        if restante == 0:   # Si no quedan escalones por subir, significa que la secuencia que se construyó es válida.
            print(f"Secuencia {c + 1}: {secuencia}")
            c += 1
        
        elif restante > 0:
            pila.insertar((restante - 1, secuencia + [1])) # Concatena a la secuencia actual el número 1, creando una nueva lista.
            pila.insertar((restante - 2, secuencia + [2]))

if __name__ == '__main__':
    tamaño = 10
    pila = PilaSecuencial(tamaño)
    calcularPeldaños(pila)