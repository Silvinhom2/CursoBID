u1 = {
    'id': 1,
    'usuario':'alicia',
    'correo':'alicia@gmail.com',
    'depto':'San Salvador',
    'rol': {1: 'Gerente', 2: 'Admin'}
}
u2 = {
    'id': 2,
    'usuario':'beto',
    'correo':'beto@gmail.com',
    'depto':'San Miguel',
    'rol': {3: 'Ventas', 4: 'Admin', 5: 'rrpp'}
}
lista_usuarios = []
lista_usuarios.append(u1)
lista_usuarios.append(u2)

# como imprimo el correo de beto a partir de la lista?
print(f'Correo de Beto: {lista_usuarios[1]["correo"]}')

# como imprimo el rol de Admin de alicia a partir de la lista?
print(f'Rol admin de alicia: {lista_usuarios[0]["rol"][2]}')

# Como imprimir todos los roles de beto a partir de la lista?
print(lista_usuarios[1]['rol'])    # opcion 1

for k,v in lista_usuarios[1]['rol'].items(): # opcion 2
    print(k,v)