from random import randint, random
import math

class Trabajo:
    __cantPaginas: int
    __tiempo: int
    __sig: int

    def __init__(self, paginas, tiempo):
        self.__cantPaginas = paginas
        self.__tiempo = tiempo
        self.__sig = None
        
    def getCantPaginas(self):
        return self.__cantPaginas
    
    def setCantPaginas(self, paginas):
        self.__cantPaginas = paginas

    def getSiguiente(self):
        return self.__sig
    
    def setSiguiente(self, siguiente):
        self.__sig = siguiente

    def getTiempo(self):
        return self.__tiempo

class ColaEncadenada:
    __primero: Trabajo
    __ultimo: Trabajo
    __cant: int

    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def recuperar(self):
        return self.__primero
    
    def insertar(self, paginas, tiempo):
        nuevo = Trabajo(paginas, tiempo)
        
        if self.vacia():
            self.__primero = nuevo
        
        else:
            self.__ultimo.setSiguiente(nuevo)
            
        self.__ultimo = nuevo
        self.__cant += 1
        # print(f"Elemento {nuevo} insertado")
        # return self.__ultimo.getItem()

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
            return None

        else:
            hojas = self.__primero.getCantPaginas()
            tiempo = self.__primero.getTiempo()
            self.__primero = self.__primero.getSiguiente()
            self.__cant -= 1

            if self.__primero is None: # Si la cola queda vacía.
                self.__ultimo = None
            # print(f"Elemento {elemento} suprimido")
            return hojas, tiempo
        
    def recorrer(self):
        if not self.vacia():
            print("\nElementos de la lista:")
            actual = self.__primero
            i = 0
            while actual != None:
                print(f"[{i}] -> {actual.getCantPaginas()}")
                actual = actual.getSiguiente()
                i += 1

        else:
            print("Cola vacía")

if __name__ == '__main__':
    cola = ColaEncadenada()
    tiempoSimulacion = 60
    reloj = 0 # Va tomando el tiempo, incrementando en uno por minuto pasado (iteración pasada).
    tiempoEspera = 0
    tiempoTotalAtencion = 0
    trabajosImpresos = 0
    trabajoSinAtender = 0
    
    while reloj < tiempoSimulacion:
        if random() <= 0.2: # 0.2 trabajos por minuto
            print("\nNuevo trabajo")
            trabajoSinAtender += 1
            hojas = randint(1, 100)
            cola.insertar(hojas, reloj) # Indica de forma aleatoria la cantidad de páginas de un trabajo.
            cola.recorrer()

        if not cola.vacia():
            trabajoActual = cola.recuperar()
            paginasAImprimir = trabajoActual.getCantPaginas()
            
            tiempoImpresion = min(paginasAImprimir / 10, 3)

            paginasImpresas = int(tiempoImpresion * 10)
            trabajoActual.setCantPaginas(paginasAImprimir - paginasImpresas)

            reloj += tiempoImpresion

            print(f"Páginas restantes del trabajo: {trabajoActual.getCantPaginas()}")

            if trabajoActual.getCantPaginas() > 0: # Cambia de trabajo
                hojas, tiempo = cola.suprimir()
                cola.insertar(hojas, tiempo)
                print("Trabajo no terminado, reingresado a la cola")
            else:
                hojas, tiempo = cola.suprimir()
                tiempoEspera = reloj - tiempo
                tiempoTotalAtencion += tiempoEspera           
                trabajosImpresos += 1
                trabajoSinAtender -= 1
                print("Trabajo finalizado")

print(f"Cantidad de trabajos sin atender: {trabajoSinAtender}")
print(f"Cantidad de trabajos impresos: {trabajosImpresos}")
if trabajosImpresos != 0:
    promedio = tiempoTotalAtencion / trabajosImpresos
else:
    promedio = 0
print(f"Tiempo promedio de espera: {promedio:.2f} minutos")