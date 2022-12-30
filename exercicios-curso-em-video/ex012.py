#Programa que lê o preço de um produto e mostra na tela qual é o preço com 5% de desconto
p = int(input('Qual o preço do produto? '))
print(f'O novo preço com 5% de desconto é {p-(p*5/100):.2f}')