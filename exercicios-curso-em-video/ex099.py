#Programa com a função maior(), que recebe vários parâmetros inteiros e analisa qual o maior
def maior(*num):
    maior = 0
    print('Analisando os valores passados:')
    for n in num:
        print(n, end=' ')
        if n > maior:
            maior = n
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.\n')


maior(0, 2, 4)
maior(7, 8, 78, 1, -4)
maior()
maior(1)