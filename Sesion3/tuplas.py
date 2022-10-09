#programa para uos de tuplas
lenguajes = ('C++','Python','PHP','JAVA')

print(len(lenguajes))
print(lenguajes)
print(lenguajes[1])
#son inmutables, sus elementos no cambian
# lenguajes[3] = 'JavaScript'     #operacion no soportada

# son estaticas, no se permite agregar y quitar eementos
# lenguajes.append(´C#')

# recorrer una tupla
for lenguaje in lenguajes:
    print('lenguaje: ',lenguaje)