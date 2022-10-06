# Hacer un programa para calcular el factorial de uun numero
# 5! = 5x4x3x2x1 = 120

n = int(input('Digite un número: '))

f = n

#for i in range(1,n):
#    f *= i

i = 1
while i<n:
    f*=i
    i+=1

print(f'El factorial de {n} es: {f}')