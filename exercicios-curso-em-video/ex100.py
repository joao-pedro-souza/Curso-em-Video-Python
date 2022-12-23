#Programa que tem uma função sorteia(), que coloca 5 números em uma lista, e uma função somaPar(), que mostra a soma dos números pares sorteados na função sorteia()
from random import randint
numeros = list()

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range (0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(n, end=' ')
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia(numeros)
somaPar(numeros)