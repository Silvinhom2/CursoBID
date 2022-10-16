from persona import Persona

alicia = Persona('Alicia','Díaz',20,'2345678986564')
beto = Persona('Beto','Pérez',16,'8978656455')

print(f'El nombre de Alicia es: {alicia.nombre}')
print(f'El apellido de Alicia es: {alicia._apellido}') # no aplica de manera forzada el ambito privado
#print(f'La edad de Alicia es: {alicia.__edad}') # es privado

alicia.mostrar_datos()
beto.mostrar_datos()

#beto.__es_adulto() # es privado, error