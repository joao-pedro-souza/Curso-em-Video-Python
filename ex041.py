from datetime import date
ano = date.today().year
nascimento= int(input('Qual seu ano de nascimento? '))
idade = ano - nascimento
print('-'*32)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-'*32)
print(f'IDADE: {idade}')
if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade > 9 and idade <= 14:
    print('CATEGORIA: INFANTIL')
elif idade > 14 and idade <= 19:
    print('CATEGORIA: JUNIOR')
elif idade > 19 and idade <= 20:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')