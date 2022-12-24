#Programa que tem uma função ficha(), que recebe dois parâmetros opcionais: nome e gols de um jogador, que mostra a ficha do jogador, mesmo que nenhum dado tenha sido informado corrretamente
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


nome = input('Nome do jogador: ')
gols = (input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    nome = '<desconhecido>'
ficha(nome, gols)