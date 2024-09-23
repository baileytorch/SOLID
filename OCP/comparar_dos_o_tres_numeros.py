def comparar_dos_o_tres_numeros(a, b, c=None):
    mayor = b
    if a > b:
        mayor = a
    if c is not None and c > mayor:
        mayor = c
    return mayor