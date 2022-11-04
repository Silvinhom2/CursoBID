''' Crear un programa que solicite N números por teclado y los guarde en una lista, a partir de la lista,
ordenarlos de menor a mayor (no se vale usar sort), mostrar el mayor, el menor, y la sumatoria y
promedio de todos'''

lista = []
def numeroIng():

    while True:
        numIng = int(input("Ingresa cualquier numero o (0 para terminar): "))
        if numIng == 0:
            break
        else:
            lista.append(numIng)
    return lista

def mayorMenor(lista): 
    mayor=0
    menor=999999
    suma = 0
    promedio = 0
    numero = 0

    for numero in lista:

        if numero>mayor:
            mayor=numero

        if numero<menor:
            menor=numero
        
        suma = suma + numero

        promedio = suma / numero


    return menor, mayor, suma, promedio


menor,mayor,suma, promedio = mayorMenor(numeroIng())
print(f"El número menor es el: {menor}, el mayor es el: {mayor}, la suma de todos es: {suma} y el promedio es: {promedio} ")