#Programa que vai perguntar ao usuário o nome e o preço de produtos, quantas vezes o usuário quiser, no final o programa vau mostrar o preço final da compra, quantos produtos custam mais de R$1000 e qual é o nome do produto mais barato.
total = mil = barato = 0
nome_barato = '0'
while True:
    nome = input('Nome do Produto: ') #Guarda o nome do produto
    preço = float(input('Preço: R$')) #Guarda o preço do produto
    total += preço #Variavel do total da compra vai receber a soma do total com o preço
    if barato == 0: #Para que o produto mais barato não custe R$0, ele vai receber o primeiro valor e nome
        barato = preço
        nome_barato = nome
    if preço < barato: #Se o preço atual for o mais barato, ele substituira o valor mais barato e o nome do produto mais barato
        barato = preço
        nome_barato = nome
    if preço > 1000: #Se o produto custar mais de R$1000, a variavel mil vai receber mais um valor
        mil += 1
    continuar = input('Quer continuar? [S/N] ').strip().upper() #Pergunta ao usuário se ele quer continuar, serão desconsiderados espaços a direita e a esquerda e a respota será jogada para maiúsculo
    if continuar == 'N': #Se a resposta for 'N' o programa será encerrado
        break
print('Fim das compras.')
print(f'Total: R${total:.2f}') #Mostra o preço total da compra
print(f'Produtos que custam mais de R$1000: {mil}') #Mostra quantos produtos custaram mais de R$1000
print(f'Produto mais barato: {nome_barato}') #Mostra o nome do produto mais barato
print(f'Preço do produto mais barato: R${barato}') #Mostra o preço do produto mais barato