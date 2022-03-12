from random import randint
vitórias = 0
while True:
    pc = randint(0,10)
    par_ou_ímpar = input('Par ou ímpar? [P/I] ')
    valor = int(input('Digite um número: '))
    soma = valor + pc
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'Você jogou {valor} e o computador {pc}. O total de {soma} deu {resultado}.')
    if par_ou_ímpar == 'P' and resultado == 'PAR' or par_ou_ímpar == 'I' and resultado == 'ÍMPAR':
        print('VOCÊ GANHOU!')
        vitórias += 1
    else:
        print('VOCÊ PERDEU')
        break
print(f'Você conseguiu {vitórias} vitórias consecutivas.')