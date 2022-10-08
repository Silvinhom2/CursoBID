'''Calcular el sueldo semanal de una persona, solicitar nombre, DUI y horas trabajadas. La hora normal
se paga en $ 10.00 hasta 40 horas, si tiene mas de 40 horas se pagan como extras al 200%. Imprima
los datos de la persona y el sueldo a remunerar'''

nombre = input('Escriba su nombre y apellido: ')
dui = input('Digite su DUI: ')
horasTrab = float(input('Ingrese las horas Trabajadas: '))
VxH = 10

if horasTrab > 40:    
    pagoNormal = 40 * VxH
    horaExtra = (horasTrab - 40) * (VxH * 2)
    pay = pagoNormal + horaExtra
    print('Hola ', nombre)
    print('Su DUI: ', dui)
    print('Su salario a remunerar es: ', pay)
else:
    pay = horasTrab * VxH
    print('Hola ', nombre)
    print('Su DUI: ', dui)
    print('Su salario a remunerar es: ', pay)