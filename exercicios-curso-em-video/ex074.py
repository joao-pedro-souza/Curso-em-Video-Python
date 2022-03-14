#Programa que gera 5 números aleatórios e coloca numa tupla, depois ele mostra os números gerados, e qual foi o maior e menor entre eles
from random import randint #Importa randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)) #Gera 5 números aleatórios e coloca numa tupla
print('Os valores sorteados foram: ', end='')
for número in n:
    print(f'{número} ', end='') #Mostra os números sorteados
print(f'\nO maior valor sorteado foi {max(n)}') #Mostra o maior valor da tupla
print(f'O menor valor sorteado foi {min(n)}') #Mostra o menor valor da tupla