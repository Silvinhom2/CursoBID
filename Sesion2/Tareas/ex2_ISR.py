# programa para calcular el inpuesto sobre la renta en El Salvador
sueldo = float(input('Digite su sueldo; '))

afp = sueldo * 0.0725
if sueldo>1000:
    iss = 1000*0.03
else:
    iss = sueldo*0.03

sg = sueldo - iss - afp
isr = 0
if sg>=0.01 and sg<=472:
    isr = 0
elif sg>=472.01 and sg<=895.24:
    isr = (sg-472)*0.01+17.67
elif sg>=895.25 and sg<=2038.10:
    isr = (sg-895.24)*0.02+60
elif sg>=2038.11:
    isr = (sg-2038.10)*0.03+288.57

print(f'El ISR a pagar es de: $ {isr:.2f}')