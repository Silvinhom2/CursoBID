# Aunque las fechas en Python ya poseen un formato legible para los humanos, en ocasiones necesitaremos ser más explícitos para no dejar espacio a la ambiguuedad, para ello, haremos uso del método strftme.
'''
    %d Día
    %m Mes
    %Y Año
    %H Hora
    %M Minutos
    %S segundos

Algo que en lo particular me gusta hacer es definir una función que me permita obtener un formato mucho más amigable.'''

from datetime import datetime

ahorita = datetime.now()
format = ahorita.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format)

def current_date_format(date):
    meses = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    dia = date.day
    mes = meses[date.month - 1]
    anio = date.year
    messsage = "{} de {} del {}".format(dia, mes, anio)

    return messsage

ahorita = datetime.now()
print(current_date_format(ahorita))