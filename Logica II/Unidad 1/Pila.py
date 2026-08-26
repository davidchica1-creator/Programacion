class Pila:

    def __init__(self, capacidad):

        self.vector = [None] * capacidad
        self.tope = -1

    def PilaVacia(self):

        if self.tope == -1:
            return True
        return False

    def PilaLlena(self):

        if self.tope == len(self.vector) - 1:
            return True
        return False

    def Apilar(self, valor):

        if self.PilaLlena():
            print("Pila llena")
            return
        else:
            self.tope += 1
            self.vector[self.tope] = valor

    def Desapilar(self):

        if self.PilaVacia():
            print("Pila vacia")
            return
        else:
            valor_eliminado = self.vector.pop(self.tope)
            self.tope -= 1
            return valor_eliminado

    def MostrarPila(self):

        if self.PilaVacia():
            print("Pila vacia")
            return
        print(f"Elementos de la pila: {self.vector}")
pila = Pila(5)

pila.Apilar(2)
pila.Apilar(3)
pila.Apilar(1)
pila.Apilar(-1)
pila.Apilar(3)

pila.MostrarPila()

pila.Desapilar()
pila.MostrarPila()