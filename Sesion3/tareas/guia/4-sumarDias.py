'''programa que solicite una fecha (día, mes, año) y una cantidad de días.
Elabore algoritmo para
sumar días a la fecha capturada'''


dia = int(input('Ingrese el DÍA actual. [Ej: 31]: '))
mes = int(input('Ingrese el MES actual. [Ej: 12]: '))
anio = int(input('Ingrese el AÑO actual. [Ej: 1990]: '))

addDay = int(input('Ingrese los días que desea avanzar: '))
newDay = dia + addDay


def fechaPropuesta(anio,mes,dia):
    bisiesto = False
    dias = newDay

    if anio % 400 == 0:
        bisiesto = True
    elif anio % 4 == 0:
        bisiesto = True

    if mes in (1,3,5,7,8,10,12):
        dias_mes = 31
    elif mes == 2:
        if bisiesto:
            dias_mes = 29
        else:
            dias_mes = 28
    else:
        dias_mes = 30

    if dias < dias_mes:
        dia += 1
        dias = dia + newDay
    else:
        dia = 1 + dias
        if mes == 12:
            mes = 1
            anio += 1
        else:
            mes += 1
        
   # newdate = print(f' Fecha prevista: {dia}, {mes}, {anio} ')
    
    return (dia, mes, anio)

#print(fechaPropuesta(2020,1,15))
#print(fechaPropuesta(2020,1,31))
print(fechaPropuesta(anio, mes, dia))

'''Aún me faltó hacerlo funcionar para que me diera la fecha actual.
Me dolió la cabeza y ya no lo continué Xb
Me estaba atrasando con el avance de los demás'''
