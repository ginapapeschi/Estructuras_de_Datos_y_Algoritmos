from ABBParaParcial import Arbol

def menu():
    print()
    print("---------- MENÚ DE OPCIONES ----------".center(90))
    try:
        op = int(input("""
[1] Insertar nodo                               [9] Evaluar si un nodo es hoja del árbol
[2] Suprimir nodo                               [10] Mostrar el grado del árbol
[3] Mostrar InOrden                             [11] Mostrar el nodo padre y hermano de un nodo ingresado
[4] Mostrar PreOrden                            [12] Mostrar la cantidad de nodos del árbol
[5] Mostrar PostOrden                           [13] Mostrar el nivel de un nodo
[6] Buscar nodo                                 [14] Mostrar la altura del árbol
[7] Evaluar si un nodo es antecesor de otro     [15] Mostrar el camino para llegar a un nodo
[8] Mostrar los sucesores de un nodo ingresado  [16] Mostrar raíz del árbol
[0] SALIR
Su opción --> """))
        return op
    except ValueError:
        print("\nERROR - El valor debe ser un número")

if __name__ == '__main__':
    arbol = Arbol()
    opcion = menu()
    
    while opcion != 0:
        if opcion == 1:  # Insertar nodo
            try:
                valor = int(input("\nIngrese el valor a insertar en el árbol: "))   
                arbol.insertar(arbol.getRaiz(), valor)           
            except ValueError:
                print("\nERROR - El valor debe ser un número")
        
        elif opcion == 2:  # Suprimir nodo
            try:
                valor = int(input("\nIngrese el valor del nodo a suprimir: "))
                arbol.suprimir(arbol.getRaiz(), valor)
                if not arbol.buscar(arbol.getRaiz(), valor):
                    print(f"Nodo {valor} eliminado")
            except ValueError:
                print("\nERROR - El valor debe ser un número")

        elif opcion == 3:  # Mostrar InOrden
            print("\nÁrbol InOrden:")
            arbol.inOrden(arbol.getRaiz())

        elif opcion == 4:  # Mostrar PreOrden
            print("\nÁrbol PreOrden:")
            arbol.preOrden(arbol.getRaiz())

        elif opcion == 5:  # Mostrar PostOrden
            print("\nÁrbol PostOrden:")
            arbol.postOrden(arbol.getRaiz())

        elif opcion == 6:  # Buscar nodo
            try:
                valor = int(input("\nIngrese el valor a buscar: "))
                nodo = arbol.buscar(arbol.getRaiz(), valor)
                if nodo:
                    print(f"El nodo {valor} existe en el árbol")
                else:
                    print(f"El nodo {valor} no se encuentra en el árbol")
            except ValueError:
                print("\nERROR - El valor debe ser un número")

        elif opcion == 7:  # Evaluar antecesor
            try:
                antecesor = int(input("\nIngrese el antecesor: "))
                valor = int(input("Ingrese el valor a verificar: "))
                if arbol.antecesor(arbol.getRaiz(), antecesor, valor):
                    print(f"{antecesor} es antecesor de {valor}")
                else:
                    print(f"{antecesor} no es antecesor de {valor}")
            except ValueError:
                print("\nERROR - Los valores deben ser números")

        elif opcion == 8:  # Mostrar sucesores
            try:
                valor = int(input("\nIngrese el valor del nodo para mostrar sus sucesores: "))
                arbol.sucesores(valor)
            except ValueError:
                print("\nERROR - El valor debe ser un número")

        elif opcion == 9:  # Evaluar si es hoja
            try:
                valor = int(input("\nIngrese el valor del nodo: "))
                if arbol.hoja(valor):
                    print(f"El nodo {valor} es hoja")
                else:
                    print(f"El nodo {valor} NO es hoja")
            except ValueError:
                print("\nERROR - El valor debe ser un número")

        elif opcion == 10:  # Mostrar grado de un nodo
            try:
                valor = int(input("\nIngrese el valor del nodo: "))
                nodo = arbol.buscar(arbol.getRaiz(), valor)
                if nodo:
                    print(f"El grado del nodo {valor} es {arbol.grado(nodo)}")
                else:
                    print(f"El nodo {valor} no existe")
            except ValueError:
                print("\nERROR - El valor debe ser un número")

        elif opcion == 11:  # Mostrar padre y hermano
            try:
                valor = int(input("\nIngrese el valor del nodo: "))
                padre, hermano = arbol.padreHermano(arbol.getRaiz(), valor)
                if padre:
                    print(f"Padre: {padre}, hermano: {hermano}")
                else:
                    print(f"No se encontró el nodo {valor}")
            except ValueError:
                print("\nERROR - El valor debe ser un número")

        elif opcion == 12:  # Mostrar cantidad de nodos
            cant = arbol.cantidadNodos(arbol.getRaiz(), 0)
            print(f"\nLa cantidad de nodos del árbol es: {cant}")

        elif opcion == 13:  # Mostrar nivel de un nodo
            try:
                valor = int(input("\nIngrese el valor del nodo: "))
                nivel = arbol.nivel(arbol.getRaiz(), valor)
                if nivel != -1:
                    print(f"El nodo {valor} está en el nivel {nivel}")
                else:
                    print(f"El nodo {valor} no se encuentra en el árbol")
            except ValueError:
                print("\nERROR - El valor debe ser un número")

        elif opcion == 14:  # Mostrar altura del árbol
            altura = arbol.altura(arbol.getRaiz())
            print(f"\nLa altura del árbol es: {altura}")

        elif opcion == 15:  # Mostrar camino a un nodo
            try:
                valor = int(input("\nIngrese el valor del nodo destino: "))
                camino = arbol.camino(arbol.getRaiz().getValor(), valor)
                if camino:
                    print(f"Camino desde la raíz hasta {valor}: {camino}")
                else:
                    print(f"No se encontró un camino hasta el nodo {valor}")
            except ValueError:
                print("\nERROR - El valor debe ser un número")

        elif opcion == 16:  # Mostrar raíz del árbol
            raiz = arbol.getRaiz()
            if raiz:
                print(f"\nLa raíz del árbol es: {raiz.getValor()}")
            else:
                print("\nEl árbol está vacío, no tiene raíz")
                
        elif type(opcion) == int:
            print("\nERROR - Opción no válida")

        opcion = menu()

    print("\nPrograma finalizado")

'''
1
10
1
5
1
3
1
7
1
8
1
9
1
20
1
15
'''