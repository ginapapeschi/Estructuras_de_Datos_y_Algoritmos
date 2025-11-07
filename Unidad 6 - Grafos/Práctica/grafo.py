import numpy as np

class Celda:
    pass

class Cola:
    pass

class Pila:
    pass

class Grafo:
    __tamaño: int
    __matriz: np.array
    __vertices: str

    def __init__(self, tamaño):
        self.__tamaño = tamaño
        self.__matriz = np.zeros((tamaño, tamaño), dtype=int)
        self.__vertices = "ABCD"
    
    def insertar(self, verticeInicial, verticeFinal):
        indiceI = self.__vertices.index(verticeInicial)
        indiceF = self.__vertices.index(verticeFinal)
        if self.__matriz[indiceI][indiceF] == 0:
            self.__matriz[indiceI][indiceF] = 1
            self.__matriz[indiceF][indiceI] = 1
        else:
            print("Ya hay relación")

    def suprimir(self, verticeInicial, verticeFinal):
        indiceI = self.__vertices.index(verticeInicial)
        indiceF = self.__vertices.index(verticeFinal)
        if self.__matriz[indiceI][indiceF] == 1:
            self.__matriz[indiceI][indiceF] = 0
            self.__matriz[indiceF][indiceI] = 0
        else:
            print("Ya está vacío")
    
    def adyacentes(self, vertice):
        indiceV = self.__vertices.index(vertice)
        adyacentes = []
        for j in range(self.__tamaño):
            if self.__matriz[indiceV][j] == 1:
                adyacentes.append(self.__vertices[j])
        return adyacentes

    def caminoEntreNodos(self, u, v):
        visitados = []
        camino = []
        band = True
        if self.busquedaEnAmplitud(u, v, camino, visitados):
            print(f"Camino de {u} a {v}:", end=" ")
            for i in camino:
                print(f"[{i}]", end=" ")
                band = True
        else:
            print(f"No existe camino de {u} a {v}")
            band = False
        return band
    

'''
TAD Grafo
TAD Digrafo
insertar Grafo
insertar Digrafo
Suprimir Grafo
Suprimir Digrafo
gradoEntrada
gradoSalida
esFuente
esSumidero
adyacentes
caminoEntreNodos
'''