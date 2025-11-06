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
    __tabla: np.ndarray

    def __init__(self, tamaño):
        self.__tamaño = self.obtenerPrimo(round(tamaño/0.7)) # Aumenta el tamaño real de la tabla para mantener el FACTOR DE CARGA menor o igual a 0.7.
        # Esto se hace porque mientras más llena esté una tabla hash, más colisiones ocurren, y el rendimiento empeora. El número primo evita que los valores del hash caigan en patrones repetitivos (distribuye mejor los índices).
        self.__tabla = np.empty(self.__tamaño, dtype=object) # Crea un arreglo vacío de LISTAS ENLAZADAS, con tamaño primo.
        for i in range(self.__tamaño):
            self.__tabla[i] = ListaEnlazada() # Asigna una lista vacía en cada índice de la tabla.
            # Cuando se inserte un elemento que COLISIONE, se lo va a encadenar dentro de la lista.

    def esPrimo(self, tamaño):
        esPrimo = True
        if tamaño < 2: # Los números menores a 2 no son primos.
            esPrimo = False
        else:
            i = 2
            while i <= int(tamaño ** 0.5) and esPrimo: # Itera desde 2 hasta la raíz cuadrada de tamaño. Si no hay divisores hasta la raíz de tamaño, no va a haber ninguno después.
                if tamaño % i == 0: # Se comprueba si tamaño es divisible entre 2 y su raíz.
                    esPrimo = False # Si encuentra un divisor, entonces no es primo.
                i += 1  
        return esPrimo

    def obtenerPrimo(self, tamaño): # Devuelve el número primo IGUAL o MAYOR al tamaño.
        if self.esPrimo(tamaño):
            resultado = tamaño # Si el tamaño ya es primo simplemente se retorna.
        else:
            siguiente = tamaño + 1 # Si no es primo se le suma uno y se pregunta hasta que esPrimo devuelva True.
            while not self.esPrimo(siguiente):
                siguiente += 1
            resultado = siguiente
        return resultado
    
    def hash(self, palabra): # Para almacenar strings
        indice = 0
        base = 31
        for letra in palabra:
            indice = (indice * base + ord(letra)) % self.__tamaño
        return indice

    def hashing(self, valor):
        return valor % self.__tamaño
    
    def insertar(self, valor):
        indice = self.hash(valor)
        self.__tabla[indice].insertar(valor)
    
    def buscar(self, valor):
        indice = self.hash(valor)
        actual = self.__tabla[indice].getCabeza()
        encontrado = False
        while actual != None and actual.getElemento() != valor:
            actual = actual.getSiguiente()
        if actual:
            encontrado = True
        return encontrado
    
    def mostrar(self): # Debug
        for i in range(self.__tamaño):
            print(f"[{i}] {self.__tabla[i]}")

if __name__ == "__main__":
    # Creamos la tabla hash
    tabla = TablaHash(5)  # tamaño pequeño para provocar colisiones rápido

    # Insertamos algunos valores
    palabras = ["hola", "adios", "hola", "python", "hash", "hashing"]
    for palabra in palabras:
        print(f"Insertando: {palabra}")
        tabla.insertar(palabra)

    print("\nTabla completa:")
    tabla.mostrar()

    # Probamos búsqueda
    test_buscar = ["hola", "python", "java"]
    for palabra in test_buscar:
        encontrado = tabla.buscar(palabra)
        print(f"¿'{palabra}' está en la tabla? -> {encontrado}")
