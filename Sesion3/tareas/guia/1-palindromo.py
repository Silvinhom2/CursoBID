'''Verificar si una palabra es palíndroma'''
# Acá solamente la palabra será ejecutada, una lo hce con frases u oraciones

cadena = input(str('Ingrese la palabra: '))

if str(cadena) == str(cadena)[::-1]: #La sintáxis de corte '[::-1]', hace que la cadena se invierta sin sesgo de corte
    print('Es Palíndromo')
else:
    print('No es Palíndromo')


# MÉTODO 2

# cadena = input(str('Ingrese la palabra: '))

# if str(cadena) == "".join(reversed(cadena)): #La sintáxis de corte '[.join(reversed]', hace que la cadena se invierta sin sesgo de corte
#     print('Es Palíndromo')
# else:
#     print('No es Palíndromo')

# Comentar en multiline crtl+k, crtl+c || Descomentar en multiline crtl+k, crtl+u