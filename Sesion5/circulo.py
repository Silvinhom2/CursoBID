from figura import Figura
import math

class Circulo(Figura):
    def __init__(self, nombre, radio):

        self.nombre = nombre
        self.radio = radio
        self.pi = 3.1416

    def mostrarNombre(self):
        print(f'La figura es: {self.nombre} ')

    def calcularArea(self):
        return self.pi*self.radio**2

    def calcularPerimetro(self):
        return 2*self.pi*self.calcularArea

    '''
    p = 2pi*a
    a = pi*r2
    '''