'''Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas
h, que indique qué hora marcará el reloj dentro de h horas'''

tiempoAct = float(input('Digite que hora es: '))
solicHoras = float(input('Digite el rango de hora a cualcular: '))

horaCalc = (tiempoAct + solicHoras) % 24
print('En ', solicHoras, ' horas, el reloj marcará las ', horaCalc)
