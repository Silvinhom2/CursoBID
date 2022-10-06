#programa para determinar si una persona es mayor de edad
#condiciones multiples

edad = int(input('Digite su edad: '))

if edad>0 and edad<18:
    print('es menor de edad')
elif edad>=18 and edad<=65:
    print('Es mayor de edad')
elif edad>65 and edad<=115:
    print('Es de tercera edad')
else:
    print('La edad no es válida')