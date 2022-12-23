#Programa que tem uma função contador() e cria três contagens: de 1 até 10 de 1 em 1, de 10 até 0 de -2 em -2 e uma contagem personalizada
def contador(i, f, p):
    if i > f:
        if p > 0:
            p = -p
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    for c in range(i, f+1, p):
        print(c, end=' ')
    print('FIM')


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é a sua vez de personalizar a contagem:')
inicio = int(input('ÍNICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
contador(inicio, fim, passo)