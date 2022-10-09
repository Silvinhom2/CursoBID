'''Programa para uso de listas'''
nombres = ['Alicia','Beto','Diana',10,[3,5,2]]

#son ordenadas
print(nombres)

#son indexadas, acceder al nombre de alicia
print(nombres[0])

#Consultar el tamaño de la lista
print(len(nombres))

#son mutables, sus elementos pueden cambiar
nombres[2] = 'Eva'
print(nombres)

#son dinámicas, se les puede agregar más elementos
nombres.append('Fran')
nombres.append('Luis')
nombres.append('Cantinflas')
print(nombres) 
nombres.remove('Beto')
nombres.pop(3)
print(nombres)

#recorrer una lista
for nombre in nombres:
    print('nombre: ', nombre)

print(nombres[2][0]) #Se lee un elemento de una lista anidada
nombres[1].pop(10)
print(nombres)
