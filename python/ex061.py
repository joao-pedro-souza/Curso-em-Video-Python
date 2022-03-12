'''n = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
n10 = n + (10) * razão
while n != n10:
    n += razão
    print(n)'''
termo = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
cont = 1
while cont < 11:
    print(f'{termo} > ', end='')
    termo += razão
    cont += 1
print('FIM')
    