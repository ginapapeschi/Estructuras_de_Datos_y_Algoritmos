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
        self.__items = np.empty(max, dtype=int)

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
            print(f"Elemento {elemento} insertado en la posición {self.__tope}")
    
    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
        
        else:
            elemento = self.__items[self.__tope]
            self.__tope -= 1
            self.__cant -= 1
            return elemento

    def mostrar(self):
        if not self.vacia():
            print("\nContenido de la pila:")
            for i in range(self.__cant - 1, -1, -1): # Recorre desde el tope hacia abajo, naturalmente LIFO.
                print(f"[{i}] -> {self.__items[i]}")
        else:
            print("Pila vacía")

if __name__ == '__main__':
    tamaño = 5
    pila = PilaSecuencial(tamaño)
    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)
    pila.insertar(5)
    pila.insertar(6)
    pila.mostrar()
    borrado = pila.suprimir()
    print(f"Elemento borrado: {borrado}")
    pila.mostrar()
    pila.insertar(6)
    pila.mostrar()