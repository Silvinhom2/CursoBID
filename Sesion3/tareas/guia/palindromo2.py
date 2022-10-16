'''Verificar si una palabra o frase es palíndroma (invierta la cadena con un while o for)'''

palindromo = input('Ingrese la palabra o frase: ')

def palindromo(oracion):
    oracion = oracion.lower()
    oracion = oracion.replace(' ', '')
    longitud = len(oracion)

    if longitud % 2 == 0:
        izquierda = oracion[:longitud // 2] # : Los 2 puntos hace que el recuento desde el primer caracter
        derecha = oracion[longitud // 2:]   # de igual manera los 2 puntos hacen que el conteo se haga hasta el final
        print('Es Palíndromo')
    else:
        izquierda = oracion[:longitud // 2]
        derecha = oracion[longitud // 2 + 1:]
        print('No es Palíndromo')

    return izquierda == derecha[::-1]


# no retorna nada aún