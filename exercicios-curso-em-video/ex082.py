#Programa que pede vários números e coloca numa lista, depois serão criadas mais 2 listas, 1 só com valores pares e outra só com valores ímpares e serão exibidas na tela
num = [] #Lista de números
par = [] #Lista de números pares
ímpar = [] #Lista de números ímpares
while True:
    num.append(int(input('Digite um número: '))) #Pede um número e o coloca na lista de números
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    if resp in 'N': #Se o usuário não quiser continuar, o programa para de pedir os números
        break
for c in range(0, len(num)): #Verifica os números na lista
    if num[c] % 2 == 0: #Se o número for par, ele será colocado na lista par
        par.append(num[c])
    else: #Senão ele será colocado na lista ímpar
        ímpar.append(num[c])
print('-'*40)
print(f'Lista de números {num}') #Mostra a lista com os números digitados
print(f'Lista de números pares {par}') #Mostra a lista de números pares
print(f'Lista de números ímpares {ímpar}') #Mostra a lista de números ímpares