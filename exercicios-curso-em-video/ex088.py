#Programa que cria palpites para Mega Sena
from random import randint
sorteio = list()
lista = list()
cont = 0
quant = int(input('Quantos sorteios quer fazer? '))
for n in range(0, quant):
    while True:
        num = randint(0, 60)
        if num not in sorteio:
            sorteio.append(num)
            cont += 1
            if cont == 6:
                cont = 0
                sorteio.sort()
                lista.append(sorteio[:])
                sorteio.clear()
                break
for x in range(0, quant):
    print(f'Jogo {x+1}: {lista[x]}')