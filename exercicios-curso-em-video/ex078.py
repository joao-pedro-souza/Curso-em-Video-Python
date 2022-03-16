#Programa que lê 5 valores e guarda numa lista, mostrando qual foi o maior e menor valor
valores = [] #Lista
maior = menor = 0 #Variáveis que guardam o maior e menor valor
for c in range(0,5):
    valores.append(int(input(f'Digite o {c+1}º valor: '))) #Pede 5 valores e os coloca na lista valores
    if menor == 0: #Atribui o primeiro valor digitado na variável menor
        menor = valores[c]
    if menor > valores[c]: #Verifica se o valor digitado é o menor
        menor = valores[c]
    elif maior < valores[c]: #Verifica se o valor digitado é o maior
        maior = valores[c]
print(valores) #Mostra a lista
print(f'O menor valor foi {menor}') #Mostra o maior valor
print(f'O maior valor foi {maior}') #Mostra o menor valor