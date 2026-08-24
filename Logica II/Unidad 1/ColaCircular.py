class ColaCircular:

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vector = [None] * capacidad
        self.primero = 0
        self.final = -1
        self.cantidad = 0

    def ColaLlena(self):
        return self.cantidad == self.capacidad

    def ColaVacia(self):
        return self.cantidad == 0

    def EncolarColaCircular(self, valor):

        if self.ColaLlena():
            print("Cola Circular está llena")
            return
        
        self.final = (self.final + 1) % self.capacidad
        self.vector[self.final] = valor
        self.cantidad += 1

    def DesencolarColaCircular(self):

        if self.ColaVacia():

            print("Cola Circular está vacía")
            return None

        valor_eliminar = self.vector[self.primero]

        if self.primero == self.final:
            self.primero = 0
            self.final = -1

        else:
            self.primero = (self.primero + 1) % self.capacidad

        self.cantidad -= 1
        return valor_eliminar

    def MostrarColaCircular(self):

        if self.ColaVacia():
            print("Cola Circular está vacía")

        else:
            elementos = []
            i = self.primero

            for _ in range(self.cantidad):
                elementos.append(self.vector[i])
                i = (i + 1) % self.capacidad

            print(elementos)

    def MostrarDesencolar(self):

        if self.ColaVacia():
            print("Cola Circular está vacía")

        else:

            vector = []
            i = self.primero

            ACTIVO = True

            while ACTIVO:

                vector.append(self.vector[i])

                if i == self.final:

                    ACTIVO = False

                else:

                    i = (i + 1) % self.capacidad

            print(vector)


Cola = ColaCircular(8)
Cola.EncolarColaCircular(2)
Cola.EncolarColaCircular(3)
Cola.EncolarColaCircular(4)
Cola.EncolarColaCircular(6)
Cola.EncolarColaCircular(8)
Cola.EncolarColaCircular(5)
Cola.EncolarColaCircular(10)
Cola.EncolarColaCircular(14)
Cola.MostrarColaCircular()

Elemento = Cola.DesencolarColaCircular()
print(Elemento)
Cola.MostrarDesencolar()

