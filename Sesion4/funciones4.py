# parametros opciionales, (valores por default)

# horas semanales 44 y se pagan extras al 200%

def sueldo(valorHora, horasTrab=44):
    sueldoPagar = 0
    if horasTrab>44:
        sueldoPagar = valorHora*44+(horasTrab-44)*valorHora*2
    else:
        sueldoPagar = valorHora*horasTrab

    return sueldoPagar

s = sueldo(10)
print(f'El sueldo a pagar es: $ {s:.2f} ')
s = sueldo(10, 48)
print(f'El sueldo a pagar es: $ {s:.2f} ')


# generacion de nombres si restriccion con "*nombres", no nos limita para agregar mas elementos
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('pedro', 'juan', 'lucas', 'simon', 'santiago')