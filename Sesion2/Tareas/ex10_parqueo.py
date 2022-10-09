'''En un estacionamiento cobran $1.50 por hora o fracción.
Escriba un programa que determine cuanto debe pagar un cliente por el estacionamiento de su vehículo, conociendo el tiempo de estacionamiento en horas y minutos'''


horas = float(input('Ingrese las horas(completas) transcurridas: '))
minutos = float(input('Ingrese los minutos restantes. Ej: 0.27...:'))
precioH = 1.50

totalH = horas * precioH
totalM = minutos * precioH
total = totalH + totalM

print('El monto a pagar por el estacionananiento es de: $', round(total,2))
print('Por las ', round(horas),' horas y ', minutos,' minutos transcurridos') 
