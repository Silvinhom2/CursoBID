'''Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y utilice las funciones para aplicar los descuentos y el IVA a los productos de la cesta y devolver el total a pagar final de la cesta.'''

canasta = []
precio = float(input('Ingrese el precio: '))
descuento = float(input('Ingrese el descuento: '))
def aplicar_descuento(precio, descuento):
    return precio - precio * descuento / 100

def aplicar_iva(precio, porcentaje):
    return precio + precio * porcentaje / 100

def dict_cantidades():
    total = 0
    for precio, descuento in canasta.items():
        total += function(precio, descuento)
    return total

print(f'''      CESTA
    El pecio de la compra tras aplicar los descuentos es: {dict_cantidades({precio, descuento}, aplicar_descuento(precio, descuento))}
    El precio de la compra tras aplicar el IVA es: {dict_cantidades({}, aplicar_iva())}''')