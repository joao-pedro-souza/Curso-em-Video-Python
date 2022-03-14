#Programa que lê 4 números e os coloca em uma tupla, ao final ele vai mostrar quantaz vezes o valor 9 apareceu, qual foi a primeira posição em que o 3 apareceu, e quais números pares foram digitados
n = (int(input('Digite um número: ')), int(input('Digite mais um número: ')), int(input('Digite outro número: ')), int(input('Digite o último número: '))) #Lê 4 números e os coloca em uma tupla
if 9 in n: #Se 9 estiver na tupla serão contadas quantas vezes ele apareceu
    print(f'O valor 9 apareceu {n.count(9)} vezes')
else: #Senão será exibida a mensagem:
    print('O valor 9 não apareceu nenhuma vez')
if 3 in n: #Se 3 apareceu na tupla será mostrada a primeira posição em que ele apareceu
    print(f'O valor 3 apareceu pela primeira vez na posição {n.index(3)+1}')
else: #Senão será exibida a mensagem:
    print('O valor 3 não apareceu em nenhuma posição')
print(f'Os números pares foram: ', end='')
for c in range(0,4):
    if n[c] % 2 == 0: #Vai verificar se os números na tupla são pares, se forem serão exibidos na tela
        print(f'{n[c]} ', end='')
    