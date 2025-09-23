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
            borrado = self.__items[self.__tope]
            self.__tope -= 1
            self.__cant -= 1
            return borrado

    def mostrar(self):
        if not self.vacia():
            print("\nContenido de la pila:")
            for i in range(self.__cant - 1, -1, -1):
                print(f"[{2**i}] -> {self.__items[i]}")
        else:
            print("Pila vacía")

def convertirABinario(numero, pila):
    if numero < 0:
        print("El número no debe ser negativo")

    #elif numero >= 256:
    #    print("No es posible la representación en binario para el número ingresado")

    elif numero == 0 or numero == 1:
        pila.insertar(numero)
        pila.mostrar()
        pila.suprimir()

    else:
        while numero > 0:
            resto = numero % 2
            pila.insertar(resto)
            numero //= 2
        
        pila.mostrar()

        while not pila.vacia():
            pila.suprimir()
        
if __name__ == '__main__':
    tamaño = 8
    pila = PilaSecuencial(tamaño)
    
    numero = int(input("Ingrese número para convertir al binario: "))
    while numero != 256:
        convertirABinario(numero, pila)
        numero = int(input("\nIngrese número para convertir al binario: "))

    print("Programa finalizado")