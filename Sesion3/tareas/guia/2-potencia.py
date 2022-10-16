'''Calcular la potencia de un número usando estructuras repetitivas, considere negativos y potencia
0'''

base = int(input('Ingrese la base de la ecuación: '))
exponencia = int(input('Ingrese el exponente de la ecuación: '))

def potencia(base, exponencia):
    resultado = 1

    for iter in range(exponencia):
        resultado *= base

    return resultado

#print(4**3)
#print(pow(4,3))
#print(potencia(4,3))
print(f'La potencia de {base} elevada a la {exponencia} es de: {potencia(base,exponencia)}')
#print(potencia(base,exponencia))