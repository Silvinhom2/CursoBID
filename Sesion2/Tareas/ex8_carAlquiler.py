'''Una compañía dedicada al alquiler de automóviles cobra un monto fijo de $30.00 para los primeros 300 km de recorrido.
Para más de 300 km y hasta 1000 km, cobra un monto adicional de $ 0.25 por cada kilómetro en exceso sobre 300.
Para más de 1000 km cobra un monto adicional de $ 0.50 por cada kilómetro en exceso sobre 1000.
Los precios ya incluyen el 13% del impuesto general a las ventas, IVA.
Escriba un programa que determine el monto a pagar por el alquiler de un vehículo y el monto incluido del impuesto.'''

km = int(input('Digite km recorridos: '))
total = 0
iva = 0

if km < 300:
    total = 30
else:
    if km > 300 and km <= 1000:
        total = 30 + (km - 300) * 0.25
    else:
        total = 30 + (km - 300) * 0.50

iva = total * 0.13
print('El monto a pagar es: ', total)
print('El IVA es: ', round(iva))
