pessoas = dict()
cadastro = list()
soma = 0
media = 0
while True:
    pessoas['Nome'] = input('Nome: ')
    pessoas['Sexo'] = input('Sexo: [M/F] ')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    r = input('Quer continuar? [S/N] ')
    cadastro.append(pessoas.copy())
    if r.lower() == 'n':
        break
print(cadastro)
print(f'O grupo tem {len(cadastro)} pessoas')
media = soma / len(cadastro)
print(f'A média de idade é de {media}')
print('As mulheres cadastradas foram: ', end='')
for c in cadastro:
    if c['Sexo'] in 'Ff':
        print(c['Nome'], end=' ')
print('\nPessoas que estão acima da média de idade: ', end='')
for c in cadastro:
    if c['Idade'] > media:
        print(c['Nome'], end=' ')