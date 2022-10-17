#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime

# Día actual
hoy = date.today()
# Fecha actual
ahorita = datetime.now()

print(hoy)
print(ahorita)

# Fecha
print("El día actual es {}".format(hoy.day))
print("El mes actual es {}".format(hoy.month))
print("El año actual es {}".format(hoy.year))


# Fecha y hora
print("El día actual es {}".format(ahorita.day))
print("El mes actual es {}".format(ahorita.month))
print("El año actual es {}".format(ahorita.year))

print(f"La hora actual es {format(ahorita.hour)}")
print(f"El minuto actual es {format(ahorita.minute)}")
print(f"El segundo actual es {format(ahorita.second)}")
