class Nodo:
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

class ListaEncadenada:
    __cabeza: Nodo
    __cant: int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    
    def vacia(self):
        return self.__cant == 0
    
    def getAnterior(self, pos):
        if 0 < pos < self.__cant:
            actual = self.__cabeza
            for i in range(pos - 1):
                actual = actual.getSiguiente()
            return actual.getItem()
        
        else: print("Posición fuera de rango"); return None
    
    def getSiguiente(self, pos):
        if 0 <= pos < self.__cant - 1:
            actual = self.__cabeza
            for i in range(pos):
                actual = actual.getSiguiente()
            return actual.getSiguiente().getItem()

        else: print("Posición fuera de rango"); return None
    
    def primerElemento(self):
        if self.vacia():
            return None
        return self.__cabeza.getItem()
    
    def ultimoElemento(self):
        if self.vacia():
            return None
        actual = self.__cabeza
        while actual.getSiguiente() != None:
            actual = actual.getSiguiente()
        return actual.getItem()

    def insertar(self, elemento):
        nuevo = Nodo(elemento)
        nuevo.setSiguiente(self.__cabeza)
        self.__cabeza = nuevo
        self.__cant += 1    
        print(f"Elemento {elemento} insertado")

    def suprimir(self, pos):
        if 0 <= pos < self.__cant:
            if not self.vacia():
                if pos == 0:
                    eliminado = self.__cabeza.getItem()
                    self.__cabeza = self.__cabeza.getSiguiente()
                else:
                    anterior = None
                    actual = self.__cabeza
                    for i in range(pos):
                        anterior = actual
                        actual = anterior.getSiguiente()
                    eliminado = actual.getItem()
                    anterior.setSiguiente(actual.getSiguiente())
                self.__cant -= 1

                print(f"Elemento en la posición {pos} eliminado: {eliminado}")
            else:
                print("Lista vacía")
        else:
            print("Posición fuera de rango")

    def recorrer(self):
        i = 0
        actual = self.__cabeza
        print("\nElementos de la lista:")
        while actual != None:
            print(f"[{i}] -> {actual.getItem()}")
            actual = actual.getSiguiente()
            i += 1
    
    def buscar(self, elemento):
        actual = self.__cabeza
        pos = 0
        while actual != None:
            if actual.getItem() == elemento:
                return pos
            actual = actual.getSiguiente()
            pos += 1
        return -1
    
    def recuperar(self, pos):
        if 0 <= pos < self.__cant:
            actual = self.__cabeza
            for i in range(pos):
                actual = actual.getSiguiente()
            return actual.getItem()
        else: print("Posición fuera de rango"); return None

if __name__ == '__main__':
    lista = ListaEncadenada()
    lista.insertar(10)
    lista.insertar(20)
    lista.insertar(30)
    lista.recorrer()
    lista.suprimir(1)
    lista.recorrer()
    print(f"Encontrado: {lista.buscar(20)}")
    print(f"Posición 1: {lista.recuperar(1)} - Anterior: {lista.getAnterior(1)} - Siguiente: {lista.getSiguiente(1)}")
        