class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaSimplementeLigada:
    def __init__(self):
        self.cabecera = None 

    def insertar(self, valor)-> None:
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def imprimir(self)-> None:
        if self.cabecera is None:
            print("La Lista Simplemente Ligada está vacia")
        else:
            nodo_actual = self.cabecera
            while nodo_actual is not None:
                print(nodo_actual.valor, end=" -> ")
                nodo_actual = nodo_actual.siguiente
            print("None")

    def eliminar(self)-> None:
        if self.cabecera is None:
            print("La LSL está vacía")
        else:
            self.cabecera = self.cabecera.siguiente

    def buscar(self, x_valor)-> bool:
        nodo_actual = self.cabecera
        pos = 0
        while nodo_actual is not None:
            if nodo_actual.valor == x_valor:
                print(f"Valor {x_valor} encontrado en la posición {pos}")
                return True
            nodo_actual = nodo_actual.siguiente
            pos += 1
        print(f"Valor {x_valor} no encontrado")
        return False

    def nodo_medio(self, inicio, fin)-> Nodo:
        if inicio is None:
            return None

        izquierda = inicio
        derecha = inicio.siguiente

        while derecha is not fin:
            derecha = derecha.siguiente
            if derecha is not fin:
                izquierda = izquierda.siguiente
                derecha = derecha.siguiente

        return izquierda

    def BusquedaBinaria(self, valor_buscado)-> None:
        nodo_actual = self.cabecera
        fin = None

        while nodo_actual is not fin:
            mitad = self.nodo_medio(nodo_actual, fin)

            if mitad is None:
                break

            if mitad.valor == valor_buscado:
                print(f"Búsqueda Binaria: ¡Valor {valor_buscado} encontrado!")
                return mitad
            elif mitad.valor < valor_buscado:
                nodo_actual = mitad.siguiente  # Buscar en la mitad derecha
            else:
                fin = mitad  # Buscar en la mitad izquierda

        print(f"Búsqueda Binaria: Valor {valor_buscado} no encontrado")
        return None


Lista = ListaSimplementeLigada()
Lista.insertar(2)
Lista.insertar(5)
Lista.insertar(10)
Lista.insertar(22)

print("--- Estado de la Lista ---")
Lista.imprimir()

print("\n--- Búsqueda Lineal ---")
Lista.buscar(2)

print("\n--- Búsqueda Binaria ---")
Lista.BusquedaBinaria(10)
Lista.BusquedaBinaria(99)  # Prueba con valor inexistente