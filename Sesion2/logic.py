# programa para uso de operadores logicos
# REGLA para la asociatividad es de izquierda a (derecha Cuando no hay parentesis) y con los parentesis, se priorizan a los mismos y lugo la ecuacion de afuera



a = 10
b = 5
c =15
print(a<b and c>=a or a!=b)
# 0 and 1 or 1
# 0 or 1
#1

print(a<b and (c>=a or a!=b))
# 0 and (1 or 1)
# 0 and 1
#0

print(not False)