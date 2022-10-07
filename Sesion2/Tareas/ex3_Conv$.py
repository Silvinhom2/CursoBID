'''
Elaborar un programa que permita realizar una conversión de monedas, sea esta de dólar a colon o viceversa, considere al menos 3 conversiones (Bitcoin) diferentes y permita al usuario seleccionar que conversión desea hacer mediante un menú.
'''
COLONDOLAR = 8.56
BITCOINDOLAR = 20000
DOLARBITCOIN = 0.00005017

def cambioDolarC(dolares):
    colon = dolares * COLONDOLAR
    return colon
def cambioColonD(colones):
    dolares = colones / COLONDOLAR
    return dolares
def cambioDolarB(dolares):
    bitcoin = dolares * DOLARBITCOIN
    return bitcoin
def cambioBitcoinD(bitcoin):
    dolar = bitcoin / DOLARBITCOIN
    return dolar
def cambioColonB(colones):
    bitcoin = colones / BITCOINDOLAR
    return bitcoin
def cambioBitcoinC(bitcoin):
    colon = bitcoin * BITCOINDOLAR
    return colon

def solicCantidad(tipo):
    cantidad = float(input(f'¿Cuánta cantidad de {tipo} vas a cambiar?'))
    return cantidad

if __name__ == '__main__':
    menu = '''
        Cambio tu moneda a cambiar.
        Selecciona una opcion
        1. Dólares a Colón
        2. Colón a Dólares
        3. Dólares a Bitcoin
        4. Bitcoin a Dólares
        5. Colón a Bitcoin
        6. Bitcoin a Colón
        7. Salir
    '''
    while True:
        opcion = int(input(menu))
        if opcion == 1:
            cantidad = solicCantidad('dólares')
            colon = round(cambioDolarC(cantidad),2)
            print(f'El resultado de cambiar {cantidad} dólares es de {colon} colones')
        elif opcion == 2:
            cantidad = solicCantidad('colones')
            dolar = round(cambioColonD(cantidad),2)
            print(f'El resultado de cambiar {cantidad} colones es de {dolar} dólares')

        elif opcion == 3:
            cantidad = solicCantidad('dólares')
            bitcoin = cambioColonD(cantidad)
            print(f'El resultado de cambiar {cantidad} dólares es de {bitcoin} bitcoins')

        elif opcion == 4:
            cantidad = solicCantidad('bitcoin')
            dolar = round(cambioColonD(cantidad),2)
            print(f'El resultado de cambiar {cantidad} bitcoins es de {dolar} dólares')
            
        elif opcion == 5:
            cantidad = solicCantidad('colones')
            bitcoin = round(cambioColonD(cantidad),8)
            print(f'El resultado de cambiar {cantidad} colones es de {bitcoin} bitcoins')
        elif opcion == 6:
            cantidad = solicCantidad('bitcoin')
            colon = round(cambioColonD(cantidad),2)
            print(f'El resultado de cambiar {cantidad} bitcoins es de {colon} colones')
        else:
            print('Hasta pronto!')
            break
# ya asi seguir agregando los datos al while



""" colonSv = input('Por favor, ingrese ingrese la cantidad de colones a convertir: ')
colonSv = float(colonSv)
dolar = 8.56

dolares = colonSv / dolar
dolares = round(dolares,2)

dolares = str(dolares) #
print('Ud. dispone de US$ ' + dolares + ' dólares') """