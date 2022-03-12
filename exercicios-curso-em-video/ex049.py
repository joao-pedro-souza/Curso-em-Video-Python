n = int(input('Digite um número: '))
d = 0
for c in range (1,n+1):
    if n%c==0:
        print(f'\33[32m{c}\33[m', end=' ' )
        d += 1
    else:
        print(f'\33[33m{c}\33[m', end=' ')
print(f'\nEsse número tem {d} divisores')
if d > 2:
    print('Esse número não é primo')
elif d == 2:
    print('Esse número é primo')