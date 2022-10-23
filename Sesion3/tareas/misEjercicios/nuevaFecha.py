# Nueva fecha
# Si nosotros así lo deseamos podemos trabajar con una fecha en particular.

'''
new_date = datetime(2019, 2, 28, 10, 15, 00, 00000)
'''
#Los argumentos serán: Año, Mes, Día, Hora, Minutos, Segundos, Milisegundos.

# En ocasiones tendremos la necesidad de realizar ciertas operaciones con fechas, ya sea agregar días, restar años o simplemente realizar comparaciones. Con Python todas estas operaciones podremos realizarlas sin ningún problema.
from datetime import datetime
from datetime import timedelta

#Sumar (dos) días a la fecha actual
masDias = int(input('Ingrese los dias a avanzar: '))
ahorita = datetime.now()
nuevaFecha = ahorita + timedelta(masDias)
print(nuevaFecha)

#Comparación
if ahorita < nuevaFecha:
    print("La fecha actual es menor que la nueva fecha")
