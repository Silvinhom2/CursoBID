# paso por valaor y por referencia

#pas por valor es por copia, inmutable
y = 2
def modifVariable(x):
    x+=10
    return x

modifVariable(y)
print(f'El valor de y es: {y}')


# paaso por referencia (direccion) mutable
v=[2,8,1,5]         # Las referecias siempre modifican al valor original
def modifArray(z):
    z.append(9)
    return z

modifArray(v)
print(f'Los valores de v son: {v} ')

w = list(v)  # asi podremos crear un nuevo array sin referencia para que no se modifique
w.append(0)
print(w, v)
print(id(w)) # podemos ver el espacio en memoria de cada lista
print(id(v))