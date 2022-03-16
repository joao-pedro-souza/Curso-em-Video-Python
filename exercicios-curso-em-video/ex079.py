#Programa que cria uma lista com números digitados pelo usuário, no final a lista é mostrada em ordem e sem números repetidos
números = [] #Lista de números
while True:
    n = int(input('Digite um número: ')) #Pede um número
    if n not in números: #O número só será adicionado se não estiver na lista
        números.append(n)
    resposta = input('Quer continuar? [S/N] ').upper().strip()[0] #Pergunta ao usuário se ele quer continuar
    if resposta in 'N':
        break
números.sort() #Ordena a lista de números
print(f'Você digitou os números {números}') #Mostra a lista