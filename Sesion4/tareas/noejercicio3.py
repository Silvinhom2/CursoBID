#'''Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la primera letra de cada palabra a mayúscula y las demás letras a minúscula, dejando inalterados los demás caracteres. Precondición: el separador de palabras es el espacio: " ". No usar la función title de Python'''


def titulo(oracion):
    oracion = ""
    first_word = True
    for letra in oracion:
        if not letra.isalpha():
            oracion = oracion + letra
            first_word = True
        else:
            if first_word:
                oracion = oracion + letra.upper()
                first_word = False
            else:
                oracion = oracion + letra.lower()
    return oracion
        