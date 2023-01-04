#Programa que gera um número aleatório entre 1 e 5, e informa se o usuário acertou o número gerado
from random import randint
from time import sleep
n = randint(1, 5)
print('==========JOGO DA ADIVINHAÇÃO==========')
r = int(input('Chute um número de 1 à 5: '))
print('CARREGANDO...')
sleep
if r == n:
    print(f'Parabéns, o número era {n}, você acertou')
else:
    print(f'O número era {n}, você errou!')


