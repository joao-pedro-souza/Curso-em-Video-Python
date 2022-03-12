mulher = 0
homem_idade = 0
homem_nome = 0
média = 0
for c in range(1,5):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: [M/F]')
    média = média + idade
    if sexo == 'F' and idade <= 20:
        mulher += 1
    elif sexo == 'M' and idade > homem_idade:
        homem_idade = idade
        homem_nome = nome
print(f'''A média de idade do grupo é {média/4:.2f}
O homem mais velho é {homem_nome} com {homem_idade} anos
{mulher} mulher(es) tem menos de 20 anos''')