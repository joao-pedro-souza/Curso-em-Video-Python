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


def resumo(n, a, r):
    print('Resumo do valor:')
    print(f'Preço analisado: {moeda(n)}')
    print(f'Dobro do preço: {dobro(n, True)}')
    print(f'Metade do preço: {metade(n, True)}')
    print(f'{a}% de aumento: {aumentar(n, a, True)}')
    print(f'{r}% de redução: {diminuir(n, r, True)}')