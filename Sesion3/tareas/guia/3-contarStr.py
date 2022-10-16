'''Contar palabras en una cadena'''


texto = input('Ingrese el texto a contar: ')

conteo = len(texto.split()) #Iniciamos variable con su metodo y la imprimimos mas abajo

#print(f'El conteo letras es de: {len(texto)} caracteres') # contamos cararcter por caracter
print(f'El conteo de palabras en la oración es de: {conteo} palabras') # contamos palabra por palabra
