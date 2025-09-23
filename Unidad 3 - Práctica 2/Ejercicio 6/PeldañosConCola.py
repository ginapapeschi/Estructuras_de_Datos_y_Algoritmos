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
        #print(f"Elemento {elemento} insertado")
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
            #print(f"Elemento {elemento} suprimido")
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

def calcularPeldaños(cola):
    c = 0
    n = int(input("Ingrese la cantidad de peldaños: "))
    cola.insertar((n, [])) # n son los peldaños RESTANTES por subir, la lista [] es la secuencia actual.

    while not cola.vacia():
        restante, secuencia = cola.suprimir() # Devuelve la última tupla en la pila.

        if restante == 0:   # Si no quedan escalones por subir, significa que la secuencia que se construyó es válida.
            print(f"Secuencia {c + 1}: {secuencia}")
            c += 1
        
        elif restante > 0:
            cola.insertar((restante - 1, secuencia + [1])) # Concatena a la secuencia actual el número 1, creando una nueva lista.
            cola.insertar((restante - 2, secuencia + [2]))

if __name__ == '__main__':
    cola = ColaEncadenada()
    calcularPeldaños(cola)

'''
Ejercicio 6: Modificar problema anterior de la escalera (resuelto utilizando un algoritmo no recursivo), pero que use una cola en lugar de pila. Compare las salidas de ambos programas.

--- SALIDA DE COLA ---
Ingrese la cantidad de peldaños: 4
Secuencia 1: [2, 2]
Secuencia 2: [1, 1, 2]
Secuencia 3: [1, 2, 1]
Secuencia 4: [2, 1, 1]
Secuencia 5: [1, 1, 1, 1]

--- SALIDA DE PILA ---
Ingrese la cantidad de peldaños: 4
Secuencia 1: [2, 2]
Secuencia 2: [2, 1, 1]
Secuencia 3: [1, 2, 1]
Secuencia 4: [1, 1, 2]
Secuencia 5: [1, 1, 1, 1]

--- COMPARACIÓN ---
Pila (LIFO): siempre toma el ÚLTIMO elemento insertado, por eso primero explora los pasos más RECIENTES agregados (2 antes que 1) → el orden es más “profundo primero” (DFS).
- Se procesa siempre el último elemento insertado.

Cola (FIFO): siempre toma el PRIMER elemento insertado, por eso primero explora los pasos más ANTIGUOS → el orden es más “amplitud primero” (BFS).
- Se procesa siempre el primer elemento insertado.

'''