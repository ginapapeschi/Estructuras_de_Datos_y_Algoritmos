import numpy as np

class PilaSecuencial:
    __dimension: int
    __incremento: int
    __tope: int
    __cantidad: int
    __items: np.ndarray

    def __init__(self, cant):
        self.__tope = -1
        self.__dimension = cant
        self.__cantidad = 0
        self.__incremento = 5
        self.__items = np.empty(self.__dimension, dtype=int)

    def vacia(self):
        return self.__tope == -1

# En insertar y suprimir siempre se ocupa el self.__tope que indica la posición del último elemento en la lista.    
    def insertar(self, elemento):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__items = np.resize(self.__items, self.__dimension)
            print(f"Dimensión aumentada a {self.__dimension}")
        
        self.__tope += 1
        self.__items[self.__tope] = elemento
        self.__cantidad += 1
        print(f"Elemento {elemento} insertado")

    def suprimir(self): 
        if self.vacia(): 
            print("Pila vacía")
        else:
            elemento = self.__items[self.__tope]
            self.__items[self.__tope] = 0  # opcional: limpiar
            self.__tope -= 1
            self.__cantidad -= 1
            print(f"Elemento {elemento} suprimido")

    def mostrar(self):
        if not self.vacia():
            print("Elementos en la pila:")
            for i in range(self.__cantidad - 1, -1, -1):
                print(f"Posición {i}: {self.__items[i]}")
        else:
            print("La pila está vacía.")

    def decimalABinario(self, numero):
        if numero < 0:
            print("El número no debe ser negativo.")
        
        if numero == 0:
            self.insertar(0)
        else:
            while numero > 0:
                resto = numero % 2
                self.insertar(resto)
                numero //= 2
            self.mostrar()

    
if __name__ == "__main__":
    pila = PilaSecuencial(8)
    pila.decimalABinario(13)
