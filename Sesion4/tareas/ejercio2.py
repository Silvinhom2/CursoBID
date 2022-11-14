'''Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".'''

correo = input('Escriba su Email: ')

def validacion():
    mail = correo

    if '@' in mail:
        print(f'Este correo ({mail}), es válido!')
    else:
        print(f'El correo ({mail}), es inválido!')

print(validacion())
