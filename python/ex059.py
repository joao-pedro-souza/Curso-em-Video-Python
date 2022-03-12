r = 6
while r != 5:
    n1 = int(input('Digite o 1º valor: '))
    n2 = int(input('Digite o 2º valor: '))
    print('''O que você deseja fazer?
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair''')
    r = int(input(''))
    if r == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}.')
    elif r ==2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}.')
    elif r ==3:
        if n1 > n2:
            print(f'{n1} é maior.')
        else:
            print(f'{n2} é maior.')