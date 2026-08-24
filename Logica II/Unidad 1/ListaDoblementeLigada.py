class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeLigada:

    def __init__(self):
        self.cabecera = None
        self.cola = None

    def eliminar_duplicados_adyacentes(self):

        nodo_actual = self.cabecera

        while nodo_actual is not None:

            representante = nodo_actual.siguiente

            while representante is not None:

                if nodo_actual.dato == representante.dato:

                    if representante.siguiente is not None:
                        representante.siguiente.anterior = representante.anterior

                    representante.anterior.siguiente = representante.siguiente

                representante = representante.siguiente

            nodo_actual = nodo_actual.siguiente