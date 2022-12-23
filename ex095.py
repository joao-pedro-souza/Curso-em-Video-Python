jogador = dict()
gols = list()
cadastro = list()
total = 0
cont = 0
njogos = 1
while True:
    jogador['Cód'] = cont
    jogador['Nome'] = input('Nome do Jogador: ')
    jogador['Jogos'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range (0, jogador['Jogos']):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = gols[:]
    for g in gols:
        total += g
    jogador['Total'] = total
    cadastro.append(jogador.copy())
    gols.clear()
    total = 0
    r = input('Quer continuar? [S/N] ')
    if r in 'Nn':
        break
    cont += 1
print('Cód'.ljust(4), end='')
print('Nome'.ljust(15), end='')
print('Gols'.ljust(15), end='')
print('Total')
for c in cadastro:
    print(f'{c["Cód"]}'.ljust(4), end='')
    print(f'{c["Nome"]}'.ljust(15), end='')
    print(f'{c["Gols"]}'.ljust(15), end='')
    print(f'{c["Total"]}')
pesquisa = int(input('Mostrar dados de qual jogador? (Insira o código) '))
for c in cadastro:
    if c['Cód'] == pesquisa:
        print(f'Levantamento do jogador {c["Nome"]}')
        for g in c['Gols']:
            print(f'No jogo {njogos} fez {g} gols')
            njogos += 1
