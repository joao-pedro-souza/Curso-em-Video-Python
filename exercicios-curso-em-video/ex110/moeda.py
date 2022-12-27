def metade(n, f=False):
    res = n / 2
    if f:
        res = moeda(res)
    return res

def dobro(n, f=False):
    res = n * 2
    if f:
        res = moeda(res)
    return res

def aumentar(n, t, f=False):
    res = n + n * t / 100
    if f:
        res = moeda(res)
    return res

def diminuir(n, t, f=False):
    res = n - n * t / 100
    if f:
        res = moeda(res)
    return res

def moeda(n):
        return f'R${n}'.replace('.', ',')
