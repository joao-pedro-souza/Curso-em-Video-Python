#Programa que pede 5 números e os ordena numa lista, sem o uso do sort()
num  = [] #Lista de números
for c in range(0,5):
    n = int(input(f'Digite o {c+1}º valor: ')) #Pede 5 valores
    if c == 0 or n > num[-1]: #Se for o primeiro valor ou o maior valor, ele será adicionado a última posição
        num.append(n)
        print('Adicionado a última posição')
    else:  
        pos = 0 #Variável que verifica a posição da lista
        while pos < len(num):
            if n <= num[pos]: #Se o número for menor ou igual ao número na posição ele será adicionado nessa posição
                num.insert(pos, n)
                print(f'Adicionado a posição {pos+1}') #Mostra a posição que o número foi inserido
                break #Se o número for adicionado o while vai ser interrompido
            pos += 1 #Aumenta a posição a ser verificada          
print(f'Você digitou os números {num}') #Mostra a lista de números