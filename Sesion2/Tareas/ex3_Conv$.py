'''
Elaborar un programa que permita realizar una conversión de monedas, sea esta de dólar a colon o viceversa, considere al menos 3 conversiones (Bitcoin) diferentes y permita al usuario seleccionar que conversión desea hacer mediante un menú.
'''
COLONDOLAR = 8.80
BITCOINDOLAR = 19385.35
DOLARBITCOIN = 0.00005200
COLONBITCOIN = 0.00000590

def cambioDolarC(dolares):
    colon = float(dolares * COLONDOLAR)
    return colon
def cambioColonD(colones):
    dolares = float(colones / COLONDOLAR)
    return dolares
def cambioDolarB(dolares):
    bitcoin = float(dolares / BITCOINDOLAR)
    return bitcoin
def cambioBitcoinD(bitcoin):
    dolar = float(bitcoin * BITCOINDOLAR)
    return dolar
def cambioColonB(colones):
    bitcoin = float(colones * COLONBITCOIN)
    return bitcoin
def cambioBitcoinC(bitcoin):
    colon = float(bitcoin / COLONBITCOIN)
    return colon

def solicCantidad(tipo):
    cantidad = float(input(f'¿Cuánta cantidad de {tipo} vas a cambiar?: '))
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
            colon = cambioDolarC(cantidad)
            print('El resultado de cambiar: $',cantidad,' dólares es de: ', round(colon,2),' colones')
        elif opcion == 2:
            cantidad = solicCantidad('colones')
            dolar = cambioColonD(cantidad)
            print('El resultado de cambiar: ',cantidad,' colones es de: $',round(dolar,2),' dólares')
        elif opcion == 3:
            cantidad = solicCantidad('dólares')
            bitcoin = cambioDolarB(cantidad)
            print('El resultado de cambiar: $',cantidad,' dólares es de: ', round(bitcoin,8),' bitcoins')
        elif opcion == 4:
            cantidad = solicCantidad('bitcoin')
            dolar = cambioBitcoinD(cantidad)
            print('El resultado de cambiar: ',cantidad,' bitcoins es de: $', round(dolar,2),' dólares')
        elif opcion == 5:
            cantidad = solicCantidad('colones')
            bitcoin = cambioColonB(cantidad)
            print('El resultado de cambiar: ', cantidad,' colones es de: ', round(bitcoin,8),' bitcoins')
        elif opcion == 6:
            cantidad = solicCantidad('bitcoin')
            colon = cambioBitcoinC(cantidad)
            print('El resultado de cambiar: ',cantidad,' bitcoins es de: ', round(colon,2),' colones')
        elif opcion == 7:
            print('Hasta pronto!')
            break