from random import randint, random
import math

class Trabajo:
    __cantPaginas: int # Cantidad de páginas restantes por imprimir.
    __tiempo: int      # Momento en el que llegó a la cola.
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
    
    def recuperar(self): # Devuelve el primer trabajo de la cola SIN ELIMINARLO.
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

    def getCantTrabajos(self):
        return self.__cant

if __name__ == '__main__':
    cola = ColaEncadenada()
    tiempoSimulacion = 60
    reloj = 0 # Va tomando el tiempo, incrementando en uno por minuto pasado (iteración pasada).
    tiempoEspera = 0
    tiempoTotalAtencion = 0 # Suma total de tiempos de espera de los trabajos impresos.
    trabajosImpresos = 0    # Contador de trabajos completados.
    tiempoDeImpresoraRestante = 3 # Controla los 3 minutos máximos que puede atender un trabajo antes de reintegrarlo a la cola.
    
    while reloj < tiempoSimulacion: # Recorre minuto a minuto la simulación.
        if random() <= 0.2: # Simula la llegada de trabajos. Probabilidad de 0.2 trabajos por minuto (1 cada 5 minutos).
            #print("\nNuevo trabajo")
            hojas = randint(1, 100) # Indica de forma aleatoria la cantidad de páginas de un trabajo (entre 1-100 páginas).
            cola.insertar(hojas, reloj) # Se inserta el trabajo en la cola con tiempo de llegada = reloj.
            #cola.recorrer()

        if not cola.vacia():
            trabajoActual = cola.recuperar() # Obtiene el primer trabajo sin quitarlo de la cola. Se utiliza como auxiliar para modificar el trabajo (con páginas restantes) sin perderlo ni sacarlo de la cola todavía.

            # Imprime hasta 10 páginas.
            paginasRestantes = trabajoActual.getCantPaginas()
            trabajoActual.setCantPaginas(max(0, paginasRestantes - 10)) # Reduce 10 páginas (velocidad de la impresora) y actualiza el trabajo actual con la nueva cantidad de páginas restantes.
            # Como la cantidad de páginas no puede ser negativa, se utiliza el max para asegurarse de que el mínimo sea 0, lo que evita bugs si las páginas restantes son menos de 10.

            tiempoDeImpresoraRestante -= 1 # Le quita un minuto del límite de tiempo máximo del trabajo.

            # Si el trabajo terminó:
            if trabajoActual.getCantPaginas() == 0:
                hojas, tiempo = cola.suprimir() # Elimina el trabajo de la cola, recuperando el tiempo de llegada.
                tiempoEspera = reloj - tiempo # reloj - tiempo de llegada.
                tiempoTotalAtencion += tiempoEspera # Suma el total y aumenta el contador de trabajos impresos.
                trabajosImpresos += 1
                # Inicia siguiente trabajo si hay disponibles en la cola.
                if not cola.vacia():
                    tiempoDeImpresoraRestante = 3 # Reinicia el contador para el siguiente trabajo.

            # Si pasaron 3 minutos y el trabajo aún tiene páginas, lo manda al final de la cola.
            elif tiempoDeImpresoraRestante == 0:
                paginasRestantes = trabajoActual.getCantPaginas()
                hojas, tiempo = cola.suprimir()
                cola.insertar(paginasRestantes, tiempo) # Se reinserta el trabajo con la cantidad de páginas actualizadas, pasados los 3 minutos.
                tiempoDeImpresoraRestante = 3 # Reinicia el contador para el siguiente trabajo.

        reloj += 1 # Avanza 1 minuto en la simulación.

    print(f"Cantidad de trabajos sin atender: {cola.getCantTrabajos()}") # Trabajos que quedan en la cola.
    print(f"Cantidad de trabajos impresos: {trabajosImpresos}")
    if trabajosImpresos != 0:
        promedio = tiempoTotalAtencion / trabajosImpresos
    else: 
        promedio = 0
    print(f"Tiempo promedio de espera: {promedio:.2f} minutos") # Promedio de tiempo de espera por trabajo impreso.

# Funcional