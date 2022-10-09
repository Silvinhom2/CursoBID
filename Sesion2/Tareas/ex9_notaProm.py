'''El promedio de prácticas de un curso se calcula en base a cuatro prácticas calificadas de las cuales se elimina la nota menor y se promedian las tres notas más altas.
Escriba un programa que determine la nota eliminada y el promedio de prácticas de un estudiante.'''

notas = []

prom = 0

for i in range(4):
  nota = int(input('Ingrese nota %d:' %(i+1)))

  notas.append(nota)

#nota menor
menor = min(notas)

print('\nLa nota menor es %d' %menor)
notas.remove(menor)

#promedio
prom = sum(notas) / 3.0
print('El promedio es %.2f' %prom)