n = int(input('Digite um número: '))
print('''Escolha a base de conversão 
[1] para binário 
[2] para octal
[3] para hexadecimal
[4] para todos''')
r = int(input('Digite sua escolha: '))
if r == 1:
    print(f'{n} em binário é igual à {bin(n)[2:]}')
elif r == 2:
    print(f'{n} em octal é igual à {oct(n)[2:]}')
elif r == 3:
    print(f'{n} em hexadecimal é igual à {hex(n)[2:]}')
else:
    print(f'''Conversão de {n}
Binário     = {bin(n)[2:]}
Octal       = {oct(n)[2:]}
Hexadecimal = {hex(n)[2:]}''')
