class ArregloDosColas:

    def __init__(self,  capacidad_total):

        mitad = capacidad_total //2

        self.total = capacidad_total
        self.capacidad = mitad
        self.vector = [None] * capacidad_total
                
        self.P1 = self.capacidad - 1
        self.F1 = -1        

        self.P2 = self.capacidad - 1
        self.F2 = self.total

    def ColaLlena(self, cola_inicial, cola_final):
        if cola_final ==  self.capacidad - 1:

            if cola_inicial == self.total:
                return True

        if cola_final == self.total - 1:

            if cola_inicial == cola_inicial:
                return True

    def ColaVacia(self, cola_inicial, cola_final):

        if cola_inicial == -1 and cola_final == self.capacidad - 1:
            return True

        if cola_inicial == self.capacidad - 1 and cola_final == self.capacidad - 1:
            return True

    def Encolar_1(self, valor):

        if self.ColaLlena(self.P1, self.F1):

            self.P1 = (self.P1 + 1) % self.capacidad
            self.vector[self.P1] = valor

        else:

            print("Cola 1 llena")

    def Encolar_2(self, valor):

        if self.ColaLlena(self.P2, self.F2):

            self.P2 = ((self.P2 - self.capacidad + 1) % (self.total - self.capacidad)) + self.capacidad
            self.vector[self.P2] = valor

        else:

            print("Cola 2 llena")

    def MostarDosColas(self):

        if self.ColaVacia(self.P1, self.F2):
            print("la Cola 2 esta vacia")

        if self.ColaVacia(self.P2, self.F2):
            print("la Cola 2 esta vacia")

        print(self.vector)


Cola = ArregloDosColas(10)

Cola.Encolar_1(5)
Cola.Encolar_1(10)
Cola.Encolar_1(15)
Cola.Encolar_1(20)
Cola.Encolar_1(25)
Cola.Encolar_1(30)

Cola.Encolar_2(100)
Cola.Encolar_2(200)


Cola.MostarDosColas()