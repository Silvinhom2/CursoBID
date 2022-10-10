
'''Ejercicio sobre colecciones

Crear un programa que capture los datos de N empleados:
-nombre
-cargo
-sueldo

Crear el siguiente menú
    1. Agregar empleado
    2. Imprimir lista
    3. Salir

para cada empleado construir un diccionario que se irá agregando a una lista que será impresa con la opción 2 del menú (usar for)
'''

menu = '''
    1. Agregar empleado
    2. Imprimir lista
    3. Salir
'''
listaEmpleados = []

i=0
while i<1:
    empleado = ()
    opcion = int(input(menu))

    if opcion == 1:
        empleado['nombre'] = input("Escriba el nombre: ")
        empleado['cargo'] = input("Escriba el cargo: ")
        empleado['sueldo'] = float(input("Escriba el sueldo: "))
        listaEmpleados.append(empleado)
    elif opcion == 2:
        print('Mostrando lista de empleados:')
        for l_e in listaEmpleados:
            print(f"Nombre: {l_e['nombre']}\n Cargo:  {l_e['cargo']}\n Sueldo: {l_e['sueldo']}")
    else:
        i+=1