from datetime import date
print('-'*20)
print('ALISTAMENTO MILITAR')
print('-'*20)
ano = date.today().year
nascimento = int(input('Qual seu ano de nascimento? '))
idade = ano - nascimento
if idade == 18:
    print('Você tem 18 anos! Hora de se alistar!')
    print(f'Você deve se alistar em {ano}')
elif idade == 17:
    print('Seu alistamento é ano que vem!')
    print(f'Você deve se alistar em {ano+1}')
elif idade < 18:
    print(f'Você é muito novo, ainda faltam {18-idade} anos para você se alistar.')
    print(f'Seu alistamento é em {ano + (18-idade)}')
elif idade == 19:
    print('Você deveria ter se alistado no ano passado!')
    print(f'Seu alistamento foi em {ano-1}')
else:
    print(f'Você já deveria ter se alistado {idade-18} anos atrás!')
    print(f'Seu alistamento foi em {ano - (idade-18)}')