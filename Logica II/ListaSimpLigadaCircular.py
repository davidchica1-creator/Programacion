class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaSimplementeLigadaCircular:
    
    def __init__(self):
        self.cabecera = None  
        self.ultimo = None

    def insertar_primer_nodo(self, valor):

        if self.ultimo is not None:
            return self.ultimo

        nuevo_nodo = Nodo(valor)

        self.ultimo = nuevo_nodo
        self.ultimo.siguiente = self.ultimo
        self.cabecera = self.ultimo
        return self.ultimo

    def insertar_inicio(self, valor):

        if self.ultimo is None:
            return self.insertar_primer_nodo(valor)

        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.ultimo.siguiente
        self.ultimo.siguiente = nuevo_nodo

        return self.ultimo
    
    def insertar_final(self, valor):

        if self.ultimo is None:

            return self.insertar_primer_nodo(valor)

        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.ultimo.siguiente
        self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo

        return self.ultimo

    def mostrar(self):

        if self.ultimo is None:
            print("LSLC está vacía")
            return None

        nodo_actual = self.ultimo.siguiente

        while nodo_actual is not None:

            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.ultimo.siguiente:
                break

        print(None)


Lista = ListaSimplementeLigadaCircular()

Lista.insertar_inicio(2)
Lista.insertar_inicio(3)
Lista.insertar_inicio(5)
Lista.insertar_inicio(2)
Lista.insertar_inicio(8)
Lista.mostrar()

Lista.insertar_final(10)
Lista.mostrar()