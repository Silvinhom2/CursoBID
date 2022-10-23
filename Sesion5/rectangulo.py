from figura import Figura

class Rectangulo(Figura):

    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base*self.altura

    def calcularPerimtetro(self):
        return 2*(self.base+self.altura)

