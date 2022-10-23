from cgi import print_arguments
from calculos import isr
from utilerias.menu import MENU
import os

print(MENU)
op = int(input('Digite una opción: '))

while(op>0 and op<7):
    sueldo = float(input('Digite el sueldo: '))
    if op==1:
        print(f'El ISSS es: $ {isr.isss(sueldo):.2f}')
    elif op==2:
        print(f'El AFP es: $ {isr.afp(sueldo):.2f} ')
    elif op==3:
        print(f'El SUELDO GRAVABLE es: $ {isr.sueldoGravable(sueldo):.2f} ')
    elif op==4:
        print(f'El ISR es: $ {isr.desc_isr(sueldo):.2f} ')
    elif op==5:
        print(f'El DESCUENTO TOTAL es: $ {isr.descuento(sueldo):.2f} ')
    elif op==6:
        print(f'El SUELDO A PAGAR es: $ {isr.sueldoPagar(sueldo):.2f} ')

    input()
    os.system('cls||clear')
    print(MENU)
    op = int(input('Digite opción: '))
    