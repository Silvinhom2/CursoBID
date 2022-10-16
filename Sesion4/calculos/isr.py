ISSS = 0.03
AFP = 0.725

def isss(sueldo):
    if sueldo>1000:
        return 30
    else:
        return sueldo*ISSS

def afp(sueldo):
    return sueldo*AFP

def sueldoGravable(sueldo):
    return sueldo-isss(sueldo)-afp(sueldo)

def desc_isr(sueldo):
    sg = sueldoGravable(sueldo)
    if sg>=0.00 and sg<=472.00:
        return 0
    elif sg>=472.01 and sg<=895.24:
        return (sg-472)*0.1+17.67
    elif sg>=895.25 and sg<=2038.10:
        return (sg-895.24)*0.02+60
    elif sg>=2038.11:
        return (sg-2038.10)*0.03+288.57
    else:
        return 0

def descuento(sueldo):
    return isss(sueldo)+afp(sueldo)+desc_isr(sueldo)

def sueldoPagar(sueldo):
    return sueldo-descuento(sueldo)