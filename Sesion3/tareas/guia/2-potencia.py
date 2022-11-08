'''Calcular la potencia de un número usando estructuras repetitivas, considere negativos y potencia
0'''

base = int(input('Ingrese el número base: '))
exponencia = int(input('Ingrese el exponente: '))

def potencia(base, exponencia):
    resultado = 1

    for iter in range(exponencia):
        resultado *= base

    return resultado

print(f'La potencia de {base} elevada a la {exponencia} es de: {potencia(base,exponencia)}')
