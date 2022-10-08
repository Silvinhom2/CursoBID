'''Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario.

Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso sobre 3.

Escriba un programa que determine el monto de la compra, el monto del descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto.'''

docenasProducto = int(input('Ingresa las docenas del producto: '))
costoUnidad = 5
montoCompra = costoUnidad * (docenasProducto * 12)

if docenasProducto > 3:
    montoDescuento = montoCompra * 0.15
    montoPagar = montoCompra - montoDescuento
elif docenasProducto <= 3:
    montoDescuento = montoCompra * 0.1
    montoPagar = montoCompra - montoDescuento

if docenasProducto > 3:
    unidadesObsequio = docenasProducto - 3
    print('Valor de la compra: ', montoCompra)
    print('Valor del descuento: ', montoDescuento)
    print('Valor a pagar: ', montoPagar)
    print('Las unidades obsequiadas fueron: ', unidadesObsequio)
else:
    unidadesObsequio = 0
    print('Valor de la compra: ', montoCompra)
    print('Valor del descuento: ', montoDescuento)
    print('Valor a pagar: ', montoPagar)
    print('Las unidades obsequiadas fueron: ', unidadesObsequio)