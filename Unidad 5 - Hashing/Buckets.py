import numpy as np 

class ListaSecuencial: # Ordenada por contenido.
    __cant: int
    __maximo: int
    __lista: np.ndarray

    def __init__(self, maximo):
        self.__maximo = maximo
        self.__cant = 0
        self.__lista = np.full(maximo, None, dtype=object)

    def vacia(self):
        return self.__cant == 0
    
    def llena(self):
        return self.__cant == self.__maximo
    
    def insertarPorContenido(self, elemento):
        if not self.llena():
            repetido = False
            if not self.vacia():
                indice = 0
                while indice < self.__cant and self.__lista[indice] != None and self.__lista[indice] < elemento:
                    indice += 1
                if self.__lista[indice] != elemento or indice == self.__cant:
                    for j in range(self.__cant, indice, -1):
                        self.__lista[j] = self.__lista[j - 1]
                    self.__lista[indice] = elemento
                
                else:
                    repetido = True
            else:
                self.__lista[0] = elemento
            
            if not repetido:
                self.__cant += 1
            
            print(f"Elemento {elemento} insertado")
        else:
            print(f"La lista está llena. El elemento {elemento} no se pudo insertar")

    def busquedaBinaria(self, elemento):
        inicio = 0
        fin = self.__cant - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.__lista[medio] == elemento:
                return True
            elif self.__lista[medio] < elemento:
                inicio = medio + 1
            else:
                fin = medio - 1
        return False

class TablaHash:
    __tamaño: int
    __tabla: np.array
    __overflow: ListaSecuencial

    def __init__(self, tamañoTabla, tamañoBucket):
        self.__tamaño = self.obtenerPrimo(round(tamañoTabla/0.7))
        self.__tabla = np.empty(self.__tamaño, dtype=object)
        for i in range(self.__tamaño):
            self.__tabla[i] = ListaSecuencial(tamañoBucket)
        self.__overflow = ListaSecuencial(round(self.__tamaño * 0.2))

    def esPrimo(self, tamaño):
        esPrimo = True
        if tamaño < 2:
            esPrimo = False
        else:
            i = 2
            while i <= int(tamaño ** 0.5) and esPrimo:
                if tamaño % i == 0:
                    esPrimo = False
                i += 1  
        return esPrimo

    def obtenerPrimo(self, tamaño):
        if self.esPrimo(tamaño):
            resultado = tamaño
        else:
            siguiente = tamaño + 1
            while not self.esPrimo(siguiente):
                siguiente += 1
            resultado = siguiente
        return resultado
    
    def hashing(self, valor):
        return valor % self.__tamaño
    
    def insertar(self, valor):
        indice = self.hashing(valor)
        if not self.__tabla[indice].llena():
            self.__tabla[indice].insertarPorContenido(valor)
        else:
            self.__overflow.insertarPorContenido(valor) 
        
    def busqueda(self, valor):
        indice = self.hashing(valor)
        encontrado = False
        if self.__tabla[indice].busquedaBinaria(valor):
            encontrado = True
        elif self.__overflow.busquedaBinaria(valor):
            encontrado = True
        return encontrado
    
if __name__ == "__main__":
    tabla = TablaHash(10, 3)

    valores = [15, 25, 35, 45, 55, 65, 75]
    for v in valores:
        tabla.insertar(v)

    print("Búsqueda de algunos valores:")
    print("25 →", tabla.busqueda(25))
    print("40 →", tabla.busqueda(40))

    print("\nContenido de la tabla:")
    for i, lista in enumerate(tabla._TablaHash__tabla):
        print(f"[{i}] -> {lista._ListaSecuencial__lista[:lista._ListaSecuencial__cant]}")
    print("Overflow ->", tabla._TablaHash__overflow._ListaSecuencial__lista[:tabla._TablaHash__overflow._ListaSecuencial__cant])
