# programa con retornos multiples y multiples valores de retorno

# retornos multiples
def dias_mes(mes):
    if mes== 12 or mes==7 or mes==8 or mes==10 or mes==5 or mes==1 or mes==3:
        return 31
    elif mes== 4 or mes==6 or mes==11:
        return 30
    elif mes==2:
        return 28
    else:
        return 0

print(dias_mes(4))

# multiples valores de retorno
def aritme(a,b):
    return a+b, a-b, a/b, a*b

print(aritme(10,5))
a = list(aritme(10,5))
print(a[2]) # asi mostramos 1 valor dentro de la lista convertida en array que se hizo arriba