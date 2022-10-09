# programa para uso de diccionarios

# nombre: valor
usuario = {
    'usuario':'alicia',
    'correo':'alicia@gmail.com',
    'depto':'San Salvador'
}

print('Usuario:', usuario['usuario'])
print(f'Correo: {usuario["correo"]}')   #formato aplicado al print
print('Dpto:', usuario['depto'])

# los elementos son mutables
usuario['usuario'] = 'alicia123'
print('Usuario modificado: ',usuario['usuario'])
# el diccionario es dinamo¿ico
usuario['telefono'] = '86746646'
print('telefono agregado: ', usuario['telefono'])
usuario.pop('depto')
print(usuario)

#recorrer el diccionario, por llaves, por valores y ambos
for llave in usuario.keys():
    print('llave', {llave})
for valor in usuario.values(): 
    print(f'valor, {valor}')    # formato aplicado al print
for llave, valor in usuario.items():
    print('llave', {llave}, 'valor: ',{valor})
