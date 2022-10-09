# programa para uso de sets

clientes = {'alicia', 'beto', 'carlos', 'daniel'}

print(len(clientes))
# son desordenados, no mantienen la posicion de su elemento
print(clientes)
# no hay acceso indexado
# print(clientes[0]) # no es posible

# clientes[1] = 'eva' # no se puede

# son de tamaño dinamico
clientes.add('eva')
print(clientes)
clientes.discard('alicia')
print(clientes) 

# recorrer el set
for cliente in clientes:
    print('cliente: ',cliente)

# no acepta repetidos pero es sencible a mayusculas(case sensitive)
clientes.add('eva')
print(clientes)

# validar la existencia de un elemento en el set
print('diana' in clientes)
print('eva' in clientes)