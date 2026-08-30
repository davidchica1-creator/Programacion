class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeLigada:

    def __init__(self):
        self.cabecera = None
        self.cola = None

    def InsertarAlInicioLDL(self, valor):
        Nuevo_nodo = Nodo(valor)
        if not self.cabecera:
            self.cabecera = Nuevo_nodo
            self.cola = Nuevo_nodo
        else:
            Nuevo_nodo.siguiente = self.cabecera
            self.cabecera.anterior = Nuevo_nodo
            self.cabecera = Nuevo_nodo

    def InsertarAlFinalLDL(self, valor):
        Nuevo_nodo = Nodo(valor)
        if not self.cola:
            self.cabecera = Nuevo_nodo
            self.cola = Nuevo_nodo
        else:
            Nuevo_nodo.anterior = self.cola
            self.cola.siguiente = Nuevo_nodo
            self.cola = Nuevo_nodo

    def EliminarAlInicioLDL(self):
        if not self.cabecera:
            return
        if self.cabecera == self.cola:
            self.cabecera = None
            self.cola = None
        else:
            Nodo_Siguiente = self.cabecera.siguiente
            Nodo_Siguiente.anterior = None
            self.cabecera = Nodo_Siguiente

    def EliminarAlFinalLDL(self):
        if not self.cola:
            return
        if self.cabecera == self.cola:
            self.cabecera = None
            self.cola = None
        else:
            Nodo_Anterior = self.cola.anterior
            Nodo_Anterior.siguiente = None
            self.cola = Nodo_Anterior

    def ImprimirLDL(self):
        Actual = self.cabecera
        while Actual:
            print(Actual.valor, end=" <--> ")
            Actual = Actual.siguiente
        print(None)

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


Lista = ListaDoblementeLigada()
Lista.InsertarAlInicioLDL(5)
Lista.InsertarAlFinalLDL(4)
Lista.InsertarAlFinalLDL(8)
Lista.InsertarAlFinalLDL(10)
Lista.InsertarAlFinalLDL(2)
Lista.ImprimirLDL()
