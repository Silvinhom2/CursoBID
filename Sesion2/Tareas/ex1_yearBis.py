# Programa que solicite el año por teclado y me diga si es bisiesto o no

year = int(input('Ingresa un año: '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('El año ', year ,' es bisiesto')
else:
    print('El año ' , year , ' no es visiesto')
    