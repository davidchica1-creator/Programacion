class ColaCircular:

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vector = [None] * capacidad
        self.primero = 0
        self.final = -1

    def ColaLlena(self):

        if self.primero == (self.final + 1) % self.capacidad:
            return True
        return False

    def ColaVacia(self):
        if self.final == -1:
            return True
        return False

    def EncolarColaCircular(self, valor):

        if self.ColaLlena():
            print("Cola Circular está llena")
            return
        
        elif self.ColaVacia():

            self.final = 0
            
        self.final = (self.final + 1) % self.capacidad
        self.vector[self.final] = valor

    def DesencolarColaCircular(self):

        if self.ColaVacia():

            print("Cola Circular está vacía")
            return None

        valor_eliminar = self.vector[self.primero]

        if self.primero == self.final:
            print("Cola Circular está vacía")
            self.primero = 0
            self.final = -1

        else:

            self.primero = (self.primero + 1) % self.capacidad

            return valor_eliminar

    def Mostrar(self):

        if self.ColaVacia():
            print("Cola Circular está vacía")

        else:

            elementos = []

            for elementos in self.vector:
                elementos.append(elementos)

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

