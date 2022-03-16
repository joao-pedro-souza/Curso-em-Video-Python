#Programa que pede vários números e coloca numa lista, depois mostra quantos números foram digitados, a lista organizada em ordem decrescente e se o valor 5 foi digitado
num = [] #Lista de números
while True:
    num.append(int(input('Digite um número: '))) #Pede um número
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    if resp in 'N': #Se o usuário não quiser continuar, o programa para de pedir números
        break
num.sort(reverse=True) #Organiza os números em ordem decrescente
print('-'*50)
print(f'Você digitou {len(num)} números') #Mostra quantos números foram digitados
print(f'Números digitados (ordem decrescente): {num}') #Mostra a lista em ordem decrescente
if 5 in num: #Se o 5 for digitado será exibida a mensagem:
    print('O valor 5 foi digitado')
else: #Senão:
    print('O valor 5 não foi digitado')