class PilaSecuencial:
    __tope: int
    __cant: int
    __items: list

    def __init__(self, cant):
        self.__tope = -1
        self.__cant = cant
        self.__items = [None] * cant

    def vacia(self):
        return self.__tope == -1
    
    def insertar(self, elemento):
        if self.__tope < self.__cant - 1:
            self.__tope += 1
            self.__items[self.__tope] = elemento
            print(f"Elemento {elemento} insertado")
        else:
            print("Pila llena")

    def suprimir(self):
        if self.vacia(): 
            print("Pila vacía")
        else:
            elemento = self.__items[self.__tope]
            self.__items[self.__tope] = None
            self.__tope -= 1
            print(f"Elemento {elemento} suprimido")
            del elemento

    def mostrar(self):
        if not self.vacia():
            print("Elementos en la pila:")
            for i in range(self.__tope, -1, -1):
                print(f"Posición {i}: {self.__items[i]}")
    
if __name__ == "__main__":
    pila = PilaSecuencial(5)
    pila.insertar(10)
    pila.insertar(20)
    pila.mostrar()
    pila.suprimir()
    pila.mostrar()