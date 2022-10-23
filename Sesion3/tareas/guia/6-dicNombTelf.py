'''Escribir un programa que vaya solicitando al usuario que ingrese nombres y telefonos.
• Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
• Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El usuario
puede utilizar la cadena "*", para salir del programa.'''

def contacto(dicc = {}):
    diccionario = {}
    if (len(dicc)):
        diccionario = dicc

    
    seguir = int(input('''
            MENÚ
        1 => Continuar
        2 => Salir
    '''))
    salir = 2
    if seguir == 1:
        nombre = input("Inserte nombre: ")
        if nombre in diccionario:
            print("Numero actual: ",diccionario[nombre])
            valor = input("   Desea modificarlo?    y   |   n:  ")

            if valor == "y":
                numero = input( "Inserte nuevo numero: ")
                diccionario[nombre] = numero
                print("Numero actualizado!")
                return contacto(diccionario)
            if valor == "n":
                return contacto(diccionario)
        else:
            numero = input("Inserte numero: ")
            diccionario.update({nombre : numero})
            print("Agregado a la agenda!")
            return contacto(diccionario)
    elif seguir == 2:
        exit(salir)

contacto()
