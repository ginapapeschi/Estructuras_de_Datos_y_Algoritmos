import numpy as np

class Celda:
    pass

class Cola:
    pass

class Pila:
    pass

class Digrafo:
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
        else:
            print("Ya hay relación")

    def suprimir(self, verticeInicial, verticeFinal):
        indiceI = self.__vertices.index(verticeInicial)
        indiceF = self.__vertices.index(verticeFinal)
        if self.__matriz[indiceI][indiceF] == 1:
            self.__matriz[indiceI][indiceF] = 0
        else:
            print("Ya está vacío")

    def gradoEntrada(self, vertice):
        indice = self.__vertices.index(vertice)
        grado = 0
        for i in range(self.__tamaño):
            if self.__matriz[i][indice] == 1:
                grado += 1
        return grado
  
    def gradoSalida(self, vertice):
        indice = self.__vertices.index(vertice)
        grado = 0
        for j in range(self.__tamaño):
            if self.__matriz[indice][j] == 1:
                grado += 1
        return grado
    
    def esFuente(self, vertice):
        return self.gradoEntrada(vertice) == 0 and self.gradoSalida(vertice) > 0
    
    def esSumidero(self, vertice):
        return self.gradoSalida(vertice) == 0 and self.gradoEntrada(vertice) > 0
    
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
        band = False
        if self.busquedaEnAmplitud(u, v, camino, visitados):
            for i in camino:
                print(i)
            band = True
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