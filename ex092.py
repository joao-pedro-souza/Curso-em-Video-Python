pessoa = dict()
pessoa['Nome'] = input('Nome: ')
pessoa['Idade'] = 2022 - int(input('Ano de Nascimento: '))
pessoa['CPTS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CPTS'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$ '))
    pessoa['Aposentadoria'] = (pessoa['Ano de contratação']+35) - (2022 - pessoa['Idade'])
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')