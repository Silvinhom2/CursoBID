'''programa que solicite una fecha (día, mes, año) y una cantidad de días, elabore algoritmo para
sumar días a la fecha capturada'''
'''
dia = int(input('Ingrese el DÍA actual. [Ej: 31]: '))
mes = int(input('Ingrese el MES actual. [Ej: 12]: '))
anio = int(input('Ingrese el AÑO actual. [Ej: 1990]: '))

#addDay = int(input('Ingrese los días que desea avanzar: '))
#newDay = dia + addDay
'''



'''
def fechaPropuesta(anio,mes,newDay):
    bisiesto = False

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

    if dia < dias_mes:
        dia += 1
    else:
        newDay = 1
        if mes == 12:
            mes = 1
            anio += 1
        else:
            mes += 1
    
    return (newDay, mes, anio)

print(fechaPropuesta(2020,1,15))
print(fechaPropuesta(2020,1,31))
#print(fechaPropuesta(anio,mes,newDay))
'''