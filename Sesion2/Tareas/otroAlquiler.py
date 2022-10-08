'''Una compañía dedicada al alquiler de automóviles cobra un monto fijo de $30.00 para los primeros 300 km de recorrido.
Para más de 300 km y hasta 1000 km, cobra un monto adicional de $ 0.25 por cada kilómetro en exceso sobre 300.
Para más de 1000 km cobra un monto adicional de $ 0.50 por cada kilómetro en exceso sobre 1000.
Los precios ya incluyen el 13% del impuesto general a las ventas, IVA.
Escriba un programa que determine el monto a pagar por el alquiler de un vehículo y el monto incluido del impuesto.'''

kmRec = float(input('Ingresa los KM recorridos: '))
montoPago = 0
montoFijo = 30
impuesto = 0.13

if kmRec <= 300:
    impCobrado = montoFijo * impuesto
    print('El monto a pagar es de: ', montoFijo)
    print('El impuesto incluido es de: ', round(impCobrado,2))
elif kmRec >= 300 and kmRec <= 1000:
    cobroAdd = 0.25 * (kmRec - 300)
    montoPago = montoFijo + cobroAdd
    impCobrado = montoPago * impuesto
    print('El monto a pagar es de: ', montoPago)
    print('El impuesto incluido es de: ', round(impCobrado))
elif kmRec > 1000:
    cobroAdd = 0.50 * (kmRec - 1000)
    montoPago = montoFijo + cobroAdd
    impCobrado = montoPago * impuesto
    print('El monto a pagar es de: ', montoPago)
    print('El impuesto incluido es de: ', round(impCobrado))
else:
    print('Adiós!!!')