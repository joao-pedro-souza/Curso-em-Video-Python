#Programa com uma tupla com a tabela do Brasileirão 2021 por ordem de colocação, o programa mostra os 5 primeiros colocados, os 4 últimos, os times em ordem alfabética, e a colocação da Chapecoense
tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'RB Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('-='*69)
print(f'Tabela do Brasileirão 2021: {tabela}') #Mostra a tupla em ordem
print('-='*69)
print(f'Os 5 primeiros times são: {tabela[0:5]}') #Mostra os 5 primeiros times
print('-='*69)
print(f'Os 4 últimos times são: {tabela[-4:]}') #Mostra os 4 últimos times
print('-='*69)
print(f'Tabela dos times em ordem alfabética: {sorted(tabela)}') #Mostra os times em ordem alfabética
print('-='*69)
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}º posição.') #Mostra a posição da Chapecoense

    