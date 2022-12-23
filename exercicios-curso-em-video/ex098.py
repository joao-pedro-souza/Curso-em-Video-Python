def contagem(i, f, p):
    if i > f:
        if p > 0:
            p = -p
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    for c in range(i, f+1, p):
        print(c, end=' ')
    print('FIM')


contagem(1, 10, 1)
contagem(10, 0, -2)
print('Agora é a sua vez de personalizar a contagem:')
inicio = int(input('ÍNICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
contagem(inicio, fim, passo)