n = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
n10 = n + (10-1) * razão
for c in range (n,n10+razão, razão):
    print(f'{c}', end=' → ')
print('ACABOU!')