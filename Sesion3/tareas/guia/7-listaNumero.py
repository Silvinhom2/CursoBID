''' Crear un programa que solicite N números por teclado y los guarde en una lista, a partir de la lista,
ordenarlos de menor a mayor (no se vale usar sort), mostrar el mayor, el menor, y la sumatoria y
promedio de todos'''

lista = []
def numeroIng():
    
    while True:
        numIng = int(input("Ingresa cualquier numero (0 para terminar): "))
        if numIng == 0:
            break
        else:
            lista.append(numIng)
    return lista

def mayorMenor(lista): 
    mayor=0
    menor=999999

    for numero in lista:

        if numero>mayor:
            mayor=numero

        if numero<menor:
            menor=numero
    return mayor,menor

#def orden(lista2):
    lista2 = numeroIng()
    numero = 0
    for numero in lista2:
        valor = numeroIng()
        lista2.append(valor)
    print('Lista sin ordenar')
    print(lista2)
    for numero in lista2:
        if lista2[numero] > lista2[numero + 1]:
            reord = lista2[numero]
            lista2[numero] = lista2[numero + 1]
            lista2[numero + 1] = reord
    print('Lista ordenada')
    print(lista2)


mayor,menor = mayorMenor(numeroIng())
#listaOrd = orden(numeroIng())
#print(f'Lista ordenada {listaOrd} ')
print(f"mayor={mayor},menor={menor}, la sumatoria y el promedio de todos es: ")