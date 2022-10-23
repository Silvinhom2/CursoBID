from rectangulo import Rectangulo
from figura import Figura
from circulo import Circulo

f = Figura('Figura')
r = Rectangulo('Rectangulo', 10, 20)
c = Circulo('Circulo', 5)

f.mostrarNombre()
r.mostrarNombre()
c.mostrarNombre()

print(f'El área de {f.nombre} es: {f.calcularArea()} ')
print(f'El área de {f.nombre} es: {f.calcularPerimtetro()} ')
print(f'El área de {r.nombre} es: {r.calcularArea()} ')
print(f'El área de {r.nombre} es: {r.calcularPerimtetro()} ')
print(f'El área de {c.nombre} es: {c.calcularArea()} ')
#print(f'El área de {c.nombre} es: {c.calcularPerimtetro()} ')