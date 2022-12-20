lista = list()
pessoas =list()
maiorpeso = 0
menorpeso =  0

while (True):
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    if peso > maiorpeso:
        maiorpeso = peso
    if menorpeso == 0:
        menorpeso = peso
    if peso < menorpeso:
        menorpeso = peso
    pessoas.append(nome)
    pessoas.append(peso)
    lista.append(pessoas[:])
    pessoas.clear()
    r = (input('Quer continuar? [S/N] '))
    if r.lower() == 'n':
        break

print(f'Quantidade de pessoas cadastradas: {len(lista)}')
print(f'O maior peso foi de {maiorpeso}kg, peso de ', end='')
for x in lista:
    if x[1] == maiorpeso:
        print(x[0], end=' ')
print(f'\nO menor peso foi de {menorpeso}kg, peso de ', end='')
for x in lista:
    if x[1] == menorpeso:
        print(x[0], end=' ')