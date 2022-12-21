lista = list()
c = 0
while True:
    c += 1
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    r = input('Quer continuar? [S/N] ')
    if r.lower() == 'n':
        break

print('Nº'.ljust(5), 'Nome'.ljust(20), 'Média')
for i, a in enumerate(lista):
    print(f'{i}'.ljust(5), f'{a[0]}'.ljust(20), f'{a[2]}')

while True:
    r = int(input('Mostrar notas de qual aluno? (999 para parar) '))
    if r == 999:
        break
    print(f'Notas de {lista[r][0]} são: {lista[r][1]}')
