#Programa que lê nome, ano de nascimento e CPTS e cadastra em um dicionário, se a CPTS for diferente de zero o dicionário também receberá ano de contratação e salário, e o cálculo de aposentadoria
from datetime import date
pessoa = dict()
pessoa['Nome'] = input('Nome: ')
pessoa['Idade'] = date.today().year - int(input('Ano de Nascimento: '))
pessoa['CPTS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CPTS'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$ '))
    pessoa['Aposentadoria'] = (pessoa['Ano de contratação']+35) - (date.today().year - pessoa['Idade'])
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')