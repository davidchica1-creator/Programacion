class ColaNoCircular:
    def __init__(self, n):
        self.capacidad = n
        self.vector = []

    def ColaVacia(self):
        return len(self.vector) == 0

    def ColaLlena(self):
        return len(self.vector) == self.capacidad

    def EncolarCNC(self, valor):
        if self.ColaLlena():
            print("CNC está llena")
            return
        else:
            nuevo_arreglo = self.vector + [valor]
            self.vector[:] = nuevo_arreglo

    def DesencolarCNC(self):
        if self.ColaVacia():
            print("CNC está vacía")
            return None
        else:
            primer_elemento = self.vector[0]
            nuevo_arreglo = self.vector[1:]  #Filtramos los datos del contenedor
            self.vector[:] = nuevo_arreglo  #Actualizamos el contenedor
            return self.vector, primer_elemento

    def Mostrar(self):
        if self.ColaVacia():
            print("CNC está vacía")
        else:
            Vector = []
            for x in self.vector:
                Vector.append(x)
            print(Vector)

    def EncolarNuevo(self, nuevo_valor):

        longitud_actual = len(self.vector)

        nuevo_arreglo = [None] * (longitud_actual + 1)

        for i in range(longitud_actual):
            nuevo_arreglo[i] = self.vector[i]

        nuevo_arreglo[longitud_actual] = nuevo_valor

        self.vector[:] = nuevo_arreglo

Cola = ColaNoCircular(8)
Cola.EncolarCNC(5)
Cola.EncolarCNC(10)
Cola.EncolarCNC(15)
Cola.EncolarCNC(20)
Cola.EncolarCNC(25)
Cola.EncolarCNC(30)
Cola.EncolarCNC(35)
Cola.EncolarCNC(40)
Cola.EncolarCNC(50)
Cola.Mostrar()

Cola.EncolarNuevo(100)
Cola.Mostrar()


Arreglo, Valor = Cola.DesencolarCNC()
Cola.Mostrar()
print("Valor = ", Valor)
