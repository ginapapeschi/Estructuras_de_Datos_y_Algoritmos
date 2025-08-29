import numpy as np

class ColaSecuencial:
    __max: int              # Total de componentes de la cola.
    __primero: int
    __ultimo: int
    __cant: int             # Cantidad actual de componentes
    __items: np.ndarray

    def __init__(self, max=0):
        self.__max = max
        self.__ultimo = 0
        self.__primero =  0
        self.__cant = 0
        self.__items = np.zeros(self.__max, dtype=int)

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, elemento):
        if self.__cant < self.__max:
            self.__items[self.__ultimo] = elemento
            self.__ultimo =  (self.__ultimo + 1) % self.__max
            self.__cant += 1
            print(f"Elemento {elemento} insertado")
            return elemento

        else:
            print("Cola llena")

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
            return None
        else:
            elemento = self.__items[self.__primero]
            self.__primero = (self.__primero + 1) % self.__max
            self.__cant -= 1
            print(f"Elemento {elemento} suprimido")
            return elemento

    def recorrer(self):
        if not self.vacia():
            print("\nElementos de la lista:")
            i = self.__primero
            for j in range(self.__cant):
                print(self.__items[i])
                i = (i + 1) % self.__max

if __name__ == '__main__':
    cola = ColaSecuencial(5)

    cola.insertar(10)
    cola.insertar(20)
    cola.insertar(30)

    cola.recorrer()

    cola.suprimir()

    cola.recorrer()
