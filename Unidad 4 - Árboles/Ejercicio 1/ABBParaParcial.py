from claseNodo import Nodo

class Arbol:
    __raiz: Nodo
    
    def __init__(self):
        self.__raiz = None
    
    def vacia(self):
        return self.__raiz == None

    def getRaiz(self):
        return self.__raiz

    def setRaiz(self, nodo):
        self.__raiz = nodo
    
    def insertar(self, nodo, valor):
        if self.vacia(): # Si el árbol está vacío crea la raíz.
            self.__raiz = Nodo(valor)
            print(f"Raíz creada - Valor {valor}")
        
        # Si el árbol no está vacío recorre desde nodo (usualmente la raíz), comparando y descendiendo por izq/der hasta encontrar un hueco, evitando insertar duplicados.
        elif nodo.getValor() == valor: # Si el valor que se quiere insertar es igual al del nodo actual.
            print("El nodo que se quiere insertar ya existe")

        elif valor < nodo.getValor(): # Si el valor que se quiere insertar es menor, va por la rama izquierda.
            if nodo.getIzq(): # Si existe un hijo izquierdo inicia la recursión, llamando a insertar sobre ese hijo.
                self.insertar(nodo.getIzq(), valor)
                # La recursión profundiza hasta encontrar la posición correcta.
            else: # Si no existe el hijo izquierdo (es None), crea uno nuevo (Nodo(valor)) y lo asigna como hijo izquierdo.
                nodo.setIzq(Nodo(valor))
                print(f"Nodo izquierdo insertado - Valor: {valor}")
        
        else: # Si el valor es mayor al valor del nodo actual, va por la rama derecha.
            if nodo.getDer(): # Si hay hijo derecho, inicia la recursión sobre él.
                self.insertar(nodo.getDer(), valor)
            else: # Si no existe el hijo deerecho, crea uno nuevo y lo asigna como hijo derecho (lo mismo que con el izquierdo).
                nodo.setDer(Nodo(valor))
                print(f"Nodo derecho insertado - Valor: {valor}")
        
    def suprimir(self, nodo, valor): # Al igual que el insertar, recibe el nodo actual y el valor a eliminar.
        resultado = nodo # Inicializa resultado con el nodo actual. Representa el NUEVO VALOR que debería ocupar esta posición del árbol después de borrar.
        # Si resultado es None, es porque el nodo eliminado era hoja y se eliminó por completo.
        # Si devuelve un nodo distinto, es porque el nodo eliminado tenía un hijo o dos, entonces el valor que devuelve resultado es el nodo que DEBE OCUPAR SU LUGAR.
        if nodo: # Verifica que el nodo exista. Si es None no hace nada, es CASO BASE de la recursión.
            if valor < nodo.getValor(): # Si el valor buscado está a la izquierda del nodo actual.
                nodo.setIzq(self.suprimir(nodo.getIzq(), valor)) # Actualiza el enlace izquierdo (setIzq) con el SUBÁRBOL RESULTANTE que devuelve la llamada recursiva a suprimir (lo seteará con la variable resultado).
            elif valor > nodo.getValor():
                nodo.setDer(self.suprimir(nodo.getDer(), valor)) # Lo mismo pero con el derecho, continuando la recursión hasta buscar el valor exacto.
                
            else: # CASO CENTRAL: se encontró el nodo cuyo valor es igual al que se QUIERE ELIMINAR (valor == nodo.getValor())
                grado = self.grado(nodo) # Calcula el grado del nodo (cuántos hijos tiene).
                if grado == 0: # Nodo hoja.
                    resultado = None # Si no tiene hijos, eliminar el nodo significa simplemente reemplazarlo por None.

                elif grado == 1: # Nodo con un solo hijo: el hijo ocupará el lugar del nodo eliminado.
                    if nodo.getDer(): # Si tiene hijo derecho, él reemplaza al nodo.
                        resultado = nodo.getDer()
                    else: 
                        resultado = nodo.getIzq() # Caso contrario, con el de la izquierda.
                    # Para actualizar el árbol vuelve al inicio en nodo.setIzq() o nodo.setDer() donde se había llamado al suprimir.

                else: # Grado == 2, nodo con dos hijos. Usa el máximo del subárbol izquierdo.
                    # No se elimina el nodo, sino que se reemplazan los valores por uno del subárbol.
                    maximo = nodo.getIzq() # Se posiciona en el subárbol izquierdo.
                    while maximo.getDer():
                        maximo = maximo.getDer() # Va buscando el máximo (el más a la derecha posible) del subárbol izquierdo.
                    nodo.setValor(maximo.getValor()) # Reemplaza el valor del nodo actual con el valor máximo encontrado.
                    nodo.setIzq(self.suprimir(nodo.getIzq(), maximo.getValor())) # Llama recursivamente a suprimir para eliminar ese NODO DUPLICADO dentro del subárbol izquierdo, ya que hasta ahora sólo se ha copiado el valor del nodo que reemplazará al nodo a eliminar.
                    # Esto eliminará el nodo que tenía el VALOR MÁXIMO ORIGINAL. Si por ejemplo se quería eliminar el 70 y el máximo encontrado es 60, ahora hay dos 60 y uno de ellos se debe eliminar (el 60 que estaba en la posición izquierda).
                    # Lo hace recursivamente ya que ese nodo con el valor máximo encontrado podría estar más abajo en el subárbol izquierdo.
                    resultado = nodo # El resultado sigue siendo el mismo nodo, pero con el VALOR ACTUALIZADO y el hijo izquierdo posiblemente modificado.

        if nodo == self.__raiz:
            self.setRaiz(resultado) # Actualiza la raíz si el nodo a eliminar era la raíz por el nuevo nodo resultante.
            # Esto asegura que self.__raiz siempre apunte a un nodo válido del árbol.
        return resultado # Devuelve el nodo que reemplaza al actual en su posición del árbol.
        # Si es hoja: devuelve None.
        # Si es un solo hijo: devuelve el hijo que reemplaza al nodo eliminado.
        # Si son dos hijos: devuelve el mismo nodo, pero con valor actualizado y subárbol izquierdo modificado si corresponde.

    def inOrden(self, nodo):    # Hijo, padre, hijo (izq - raíz - der). ORDEN ASCENDENTE.
        if nodo: # Caso base: si es None la recursión termina.
            self.inOrden(nodo.getIzq()) # Llama recursivamente al subárbol izquierdo, recorriendo todos los nodos de la izquierda antes de procesar el nodo actual.
            print(nodo.getValor()) # Imprime el valor del nodo actual después de haber recorrido la izquierda.
            self.inOrden(nodo.getDer()) # Llama recursivamente al subárbol derecho. Recorre todos los nodos de la derecha después de procesar el nodo actual.

    def preOrden(self, nodo):   # Primero padre, luego hijos (raíz - izq - der). SIGUE LA ESTRUCTURA DEL ÁRBOL.
        if nodo:
            print(nodo.getValor()) # Imprime el valor del nodo actual ANTES de recorrer sus hijos.
            self.preOrden(nodo.getIzq()) # Llama al subárbol izquierdo y recorre todos los nodos de la izquierda después de imprimir el nodo actual.
            self.preOrden(nodo.getDer()) # Recorre todos los nodos de la derecha después de procesar el nodo y su subárbol izquierdo.
    
    def postOrden(self, nodo):  # Primero hijos, después el padre (izq - der - raíz). DESDE LAS HOJAS HASTA LA RAÍZ.
        if nodo:
            self.postOrden(nodo.getIzq())
            self.postOrden(nodo.getDer())
            print(nodo.getValor())
            # Primero baja a los hijos y sólo imprime el nodo actual (por lo general, la raíz) cuando ya procesó todos sus descendientes.

    def buscar(self, nodo, valor): # Recibe los mismos parámetros que insertar y suprimir.
        if not nodo: # Caso base: hasta no encontrarse va a seguir iterando.
            nodoEncontrado = None # Si el nodo actual es None, significa que se llegó al final del árbol sin encontrar el valor.
        elif nodo.getValor() == valor: # Caso de éxito: se encontró el nodo y lo guarda como resultado.
            nodoEncontrado = nodo
        elif valor < nodo.getValor(): # Si el valor buscado es menor, recursa sobre el subárbol izquierdo.
            nodoEncontrado = self.buscar(nodo.getIzq(), valor)
        else:
            nodoEncontrado = self.buscar(nodo.getDer(), valor) # Lo mismo, pero con el derecho.
        return nodoEncontrado

    def antecesor(self, nodo, antecesor, valor):
        resultado = False
        if nodo: # Caso base. Si llega a None, recorrió toda la rama sin éxito.
            if nodo.getValor() == antecesor: # Se encontró el nodo que podría ser antecesor.
                encontrado = self.buscar(nodo, valor) # Se verifica si el valor buscado está en su subárbol para verificar que SÍ está antes que el valor buscado, de lo contrario no lo antecede.
                if encontrado:
                    resultado = True
            else: # Se sigue buscando en subárboles.
                if valor < nodo.getValor(): # Sigue buscando rescursivamente por izquierda y por derecha.
                    resultado = self.antecesor(nodo.getIzq(), antecesor, valor)
                else:
                    resultado = self.antecesor(nodo.getDer(), antecesor, valor)
        return resultado
    
    def sucesores(self, valor): # Mira los nodos que descienden del lado DERECHO del árbol. Es decir, dado un valor, mostrar los nodos que vienen después de él en el árbol.
        nodo = self.buscar(self.__raiz, valor) # Verifica que el valor existe en el árbol.
        if nodo: # Si el valor fue hallado en el árbol (el nodo existe).
            if nodo.getDer(): # Si el nodo tiene HIJO DERECHO, entonces tiene sucesores.
                self.preOrden(nodo.getDer()) # Recursa sobre preOrden que muestra todos los nodos que le suceden a valor automáticamente.
            else:
                print(f"No hay sucesores de {valor}")
        else:
            print(f"El nodo con valor {valor} no existe en el árbol")

    def relacionPadreHijo(self, padre, hijo): # Determina si un nodo con cierto valor (padre) tiene como HIJO DIRECTO (izquierdo o derecho) a otro nodo (hijo).
        resultado = False
        nodoPadre = self.buscar(self.__raiz, padre) # Busca el nodo con el valor del POSIBLE PADRE para verificar que exista.
        if nodoPadre: # Si existe el nodo con el valor del padre ingresado.
            if nodoPadre.getIzq() and nodoPadre.getIzq().getValor() == hijo: # Verifica si el hijo izquierdo EXISTE y si coincide con el valor del HIJO INGRESADO.
                resultado = True
            if nodoPadre.getDer() and nodoPadre.getDer().getValor() == hijo: # Hace lo mismo para el hijo derecho.
                resultado = True
        return resultado
    
    # Interfaces semánticas que REUTILIZAN EL MISMO MÉTODO para mayor legibilidad.
    def padre(self, padre, hijo):
        return self.relacionPadreHijo(padre, hijo)
    def hijo(self, hijo, padre):
        return self.relacionPadreHijo(padre, hijo) # Invierte los parámetros para verificar si el valor pasado como "padre" realmente lo es. Sólo se invierten para cambiar la semántica de la función, pero funciona exactamente igual.

    def padreHermano(self, nodo, valor): # Parámetros igual que insertar, suprimir y buscar.
        padre, hermano = None, None # Se utilizan banderas que posteriormente se retornarán como tupla.
        if nodo: # Caso base.
            if nodo.getIzq() and nodo.getIzq().getValor() == valor: # Si existe el hijo izquierdo del nodo actual y su valor coincide con el buscado. -- Misma condición que en relacionPadreHijo().
                padre = nodo.getValor() # Entonces el nodo actual es el PADRE.
                if nodo.getDer(): # Si existe el hijo derecho, entonces es el nodo HERMANO.
                    hermano = nodo.getDer().getValor()

            elif nodo.getDer() and nodo.getDer().getValor() == valor: # El valor está en el hijo derecho. Se hace lo mismo, pero al revés.
                padre = nodo.getValor()
                if nodo.getIzq():
                    hermano = nodo.getIzq().getValor()

            # Si aún no se encontró el valor se recursa.
            elif valor < nodo.getValor(): # Si el valor buscado es menor que el actual.
                p, h = self.padreHermano(nodo.getIzq(), valor) # Recursión en subárbol izquierdo. Si está, devolverá el padre y el hermano que corresponden a ese nodo.
                if p: # Si después de la recursión se obtiene un resultado válido.
                # p contiene el PADRE del NODO BUSCADO que encontró la llamada recursiva. h contiene el nodo del hermano, SI ES QUE EXISTE. Por eso no se utiliza como condición, porque puede no existir.
                # Si p es None, significa que el nodo NO ESTABA en ese subárbol, entonces no se cambia nada y no se envía ningún valor nuevo de retorno al desapilarse cada recursión. 
                    padre, hermano = p, h # Si encuentra algo, devuelve el padre y el hermano encontrados. Es decir, toma el resultado que vino desde los nodos más profundos y lo asigna a las variables locales de nivel superior.
            
            elif valor > nodo.getValor(): # Si el valor buscado es mayor que el actual.
                p, h = self.padreHermano(nodo.getDer(), valor) # Recursión en subárbol derecho.
                if p:
                    padre, hermano = p, h

        return padre, hermano # Retorna una tupla.

    def hoja(self, valor): # Determina si un nodo con un VALOR ESPECÍFICO es una hoja en el árbol (no tiene hijos).
        nodo = self.buscar(self.__raiz, valor) # Busca el nodo con el valor dado en todo el árbol.
        return nodo is not None and self.grado(nodo) == 0 # Verifica que el nodo EXISTA en el árbol y que su grado sea 0, que indica que NO TIENE HIJOS, por lo tanto, es hoja.
            
    def grado(self, nodo): # MÉTODO IMPORTANTE - Determina la cantidad de hijos de un nodo.
        grado = 0
        if nodo.getIzq(): # Si existe un hijo izquierdo, suma 1 al grado.
            grado += 1
        if nodo.getDer(): # Lo mismo si existe un hijo derecho.
            grado += 1
        return grado

    def nivel(self, nodo, valor, nivel=1): # nivel=1 asegura que mínimamente el nivel de un nodo sea 1 y no 0. Se usa como un static.
        resultado = -1 # En caso de NO EXISTIR el nodo.
        if nodo: # Caso base.
            if nodo.getValor() == valor: # Caso exitoso: si se encuentra el nodo buscado, se retorna el NIVEL ACTUAL. Es un buscar() implícito.
                resultado = nivel
            elif valor < nodo.getValor(): # Si el valor buscado es MENOR que el nodo actual inicia la recursión.
                resultado = self.nivel(nodo.getIzq(), valor, nivel + 1) # Baja al subárbol izquierdo y aumenta en 1 su nivel (porque se está un nivel más abajo en el árbol).
            else:
                resultado = self.nivel(nodo.getDer(), valor, nivel + 1) # Baja al subárbol derecho, también aumenta el nivel.

        return resultado
    
    def altura(self, nodo): # La altura de un nodo es la DISTANCIA MÁXIMA desde ese nodo hasta una hoja.
        # Un nodo hoja tiene altura = 1, y un nodo con hijos tiene altura = 1 + altura máxima de sus subárboles.
        maxAltura = 0
        if nodo: # Caso base.
            alturaIzq = self.altura(nodo.getIzq()) # Llama recursivamente a altura() sobre el hijo izq y der.
            alturaDer = self.altura(nodo.getDer()) # Esto desciende a las HOJAS, calculando la altura de cada subárbol.
            maxAltura = 1 + max(alturaIzq, alturaDer) # El nodo actual cuenta como 1 (por convención, podría ser 0), se le suma la MAYOR entre las dos alturas de ambos subárboles.
        return maxAltura

    def camino(self, inicio:int, fin:int): # Se busca obtener la SECUENCIA de movimientos desde un nodo inicio hasta un nodo fin.
        esAntecesor = self.antecesor(self.__raiz, inicio, fin) # Verifica si el nodo inicio es ANTECESOR de fin.
        camino = [] # Devuelve una lista vacía si INICIO no es ANTECESOR de FIN (es decir, si fin no está en el subárbol de inicio)
        if esAntecesor:
            nodoActual = self.buscar(self.__raiz, inicio) # Si inicio es antecesor, busca el nodo inicio para empezar desde ahí. Es necesario verificarlo para empezar desde el nodo correcto, ya que antecesor() sólo devuelve True o False.
            while nodoActual and nodoActual.getValor() != fin: # Recorre el árbol desde el nodo inicio hasta llegar a fin.
                if fin < nodoActual.getValor(): # Si el valor del fin es menor al nodo actual, se va a la izquierda.
                    camino.append(0) # Va a la izquierda (da un paso en el recorrido).
                    nodoActual = nodoActual.getIzq()
                else:
                    camino.append(1) # Va a la derecha
                    nodoActual = nodoActual.getDer() # Si es mayor, se va a la derecha.
        return camino
    
    def cantidadNodos(self, nodo, cant):
        if nodo:
            cant = self.cantidadNodos(nodo.getIzq(), cant)
            cant += 1
            cant = self.cantidadNodos(nodo.getDer(), cant)
        return cant

'''
if __name__ == '__main__':
    arbol = Arbol()
    arbol.insertar(arbol.getRaiz(), 10)
    arbol.insertar(arbol.getRaiz(), 5)
    arbol.insertar(arbol.getRaiz(), 3)
    arbol.insertar(arbol.getRaiz(), 7)
    arbol.insertar(arbol.getRaiz(), 20)
    arbol.insertar(arbol.getRaiz(), 8)
    arbol.insertar(arbol.getRaiz(), 9)
    print("Inorden:")
    arbol.inOrden(arbol.getRaiz())
    print("PreOrden:")
    arbol.preOrden(arbol.getRaiz())
    print("PostOrden:")
    arbol.postOrden(arbol.getRaiz())
    encontrado = arbol.buscar(arbol.getRaiz(), 3)
    if encontrado:
        print(f"Valor encontrado: {encontrado.getValor()}")
    else:
        print("No se encontró el valor en el árbol")
    
    nivel = arbol.nivel(arbol.getRaiz(), 10)
    if nivel != -1:
        print(f"Nivel del nodo 10: {nivel}")
    else: print("El nodo con el valor ingresado no se encuentra en el árbol")
    print(f"Altura del árbol: {arbol.altura(arbol.getRaiz())}")

    antecesor = arbol.antecesor(arbol.getRaiz(), 10, 3)
    if antecesor:
        print("Es antecesor")
    else:
        print("No es antecesor")
    
    camino = (arbol.camino(10, 3))
    if camino:
        print(f"Camino: {camino}")
    else:
        print("No existe camino: el inicio no es antecesor del fin")

    print("\nSucesores:")
    arbol.sucesores(5)

    print("\nÁrbol antes de eliminar:")
    arbol.preOrden(arbol.getRaiz())
    arbol.suprimir(arbol.getRaiz(), 3)
    print("Árbol tras eliminar:")
    arbol.preOrden(arbol.getRaiz())
    print(f"Raíz del árbol: {arbol.getRaiz().getValor()}")
    print("Eliminando la raíz")
    arbol.suprimir(arbol.getRaiz(), 10)
    print(f"Nueva raíz: {arbol.getRaiz().getValor()}")
    print("Árbol tras eliminar la raíz:")
    arbol.preOrden(arbol.getRaiz())
'''