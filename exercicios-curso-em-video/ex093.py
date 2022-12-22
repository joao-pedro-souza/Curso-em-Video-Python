jogador = dict()
gols = list()
total = 0
jogador['Nome'] = input('Digite o nome do jogador: ')
jogador['Jogos'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, jogador['Jogos']):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['Gols'] = gols
for c in gols:
    total += c
jogador['Total'] = total
print(f'O jogador {jogador["Nome"]} fez {jogador["Jogos"]} jogos.')
for c in range(0, jogador['Jogos']):
    print(f'Na partida {c+1} fez {jogador["Gols"][c]}')