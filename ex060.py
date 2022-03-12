"""""n = int(input('Digite um número: '))
n2 = n-1
f = n
while n2 != 1:
    n = n*n2
    n2 -= 1
print(f'{f}! é igual à {n}')"""
from math import factorial
n = int(input('Digite um número: '))
c = n
print(f'Calculando fatorial {n}!')
while c > 0:
    print(f'{c}', end='')
    print('x' if c > 1 else '=', end='')
    c -= 1
print(f'\n O fatorial de {n} é {factorial(n)}')