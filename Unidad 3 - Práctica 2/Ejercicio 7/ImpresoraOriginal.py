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

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
            return None
        else:
            hojas = self.__primero.getCantPaginas()
            tiempo = self.__primero.getTiempo()
            self.__primero = self.__primero.getSiguiente()
            self.__cant -= 1
            if self.__primero is None:  # Si la cola queda vacía.
                self.__ultimo = None
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
    reloj = 0  # Tiempo global
    tiempoEspera = 0
    tiempoTotalAtencion = 0
    trabajosImpresos = 0
    trabajoSinAtender = 0

    while reloj < tiempoSimulacion:
        # Generar trabajos con probabilidad 0.2
        if random() <= 0.2:
            print("\nNuevo trabajo")
            trabajoSinAtender += 1
            hojas = randint(1, 100)
            cola.insertar(hojas, reloj)
            cola.recorrer()

        if not cola.vacia():
            paginasAImprimir = cola.recuperar().getCantPaginas()

            if paginasAImprimir < 30:
                print("Trabajo con menos de 30 páginas")

                if paginasAImprimir < 10:
                    # Consume el tiempo real proporcional
                    tiempo_consumido = math.ceil(paginasAImprimir / 10)
                    cola.recuperar().setCantPaginas(0)
                    reloj += tiempo_consumido
                    print(f"Trabajo terminado en {tiempo_consumido} minutos")
                    
                    hojas, tiempo = cola.suprimir()
                    tiempoEspera = reloj - tiempo
                    tiempoTotalAtencion += tiempoEspera
                    trabajosImpresos += 1
                    trabajoSinAtender -= 1
                    print("Trabajo finalizado")
                
                else:
                    # Se imprimen 10 páginas en 1 minuto
                    cola.recuperar().setCantPaginas(paginasAImprimir - 10)
                    reloj += 1
                    print(f"Páginas restantes: {cola.recuperar().getCantPaginas()}")

            else:
                # Trabajo grande (round robin: 30 páginas en 3 min)
                print("Trabajo con más de 30 páginas")
                cola.recuperar().setCantPaginas(paginasAImprimir - 30)
                reloj += 3
                print(f"Páginas restantes: {cola.recuperar().getCantPaginas()}")

                paginasRestantes = cola.recuperar().getCantPaginas()
                if paginasRestantes > 0:
                    hojas, tiempo = cola.suprimir()
                    cola.insertar(hojas, tiempo)  # vuelve al final
                    print("Cambia de trabajo")
                else:
                    hojas, tiempo = cola.suprimir()
                    tiempoEspera = reloj - tiempo
                    tiempoTotalAtencion += tiempoEspera
                    trabajosImpresos += 1
                    trabajoSinAtender -= 1
                    print("Trabajo finalizado")
        else:
            reloj += 1  # Avanza el tiempo si no hay trabajos

    print(f"\nCantidad de trabajos sin atender: {trabajoSinAtender}")
    print(f"Cantidad de trabajos impresos: {trabajosImpresos}")
    if trabajosImpresos != 0:
        promedio = tiempoTotalAtencion / trabajosImpresos
    else:
        promedio = 0
    print(f"Tiempo promedio de espera: {promedio:.2f} minutos")
