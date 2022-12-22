dicionario = dict()
dicionario['Nome'] = input('Nome do aluno: ')
dicionario['Média'] = float(input('Média do aluno: '))
if dicionario['Média'] >= 5:
    dicionario['Situação'] = 'Aprovado'
else:
    dicionario['Situação'] = 'Reprovado' 
for k, v in dicionario.items():
    print(f'{k} é igual a {v}')