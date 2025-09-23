class Celda:
    __item: int
    __sig: int

    def __init__(self, item):
        self.__item = item
        self.__sig = None

    def getItem(self):
        return self.__item
    
    def setItem(self, item):
        self.__item = item

    def getSiguiente(self):
        return self.__sig
    
    def setSiguiente(self, siguiente):
        self.__sig = siguiente

class ColaEncadenada:
    __primero: Celda
    __ultimo: Celda
    __cant: int

    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def recuperar(self):
        return self.__primero
    
    def insertar(self, elemento):
        nuevo = Celda(elemento)
        
        if self.vacia():
            self.__primero = nuevo
        
        else:
            self.__ultimo.setSiguiente(nuevo)
            
        self.__ultimo = nuevo
        self.__cant += 1
        print(f"Elemento {elemento} insertado")
        return self.__ultimo.getItem()

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
            return None

        else:
            elemento = self.__primero.getItem()
            self.__primero = self.__primero.getSiguiente()
            self.__cant -= 1

            if self.__primero is None: # Si la cola queda vacía.
                self.__ultimo = None
            print(f"Elemento {elemento} suprimido")
            return elemento
        
    def recorrer(self):
        if not self.vacia():
            print("\nElementos de la lista:")
            actual = self.__primero
            i = 0
            while actual != None:
                print(f"[{i}] -> {actual.getItem()}")
                actual = actual.getSiguiente()
                i += 1

        else:
            print("Cola vacía")

if __name__ == '__main__':
    cola = ColaEncadenada()
    cola.recorrer()
    cola.insertar(10)
    cola.insertar(20)
    cola.insertar(30)
    cola.insertar(40)
    cola.insertar(50)
    cola.recorrer()
    print(f"\nPrimer elemento en la cola: {cola.recuperar().getItem()}")
    cola.suprimir()
    print(f"\nPrimer elemento en la cola: {cola.recuperar().getItem()}")
    cola.recorrer()