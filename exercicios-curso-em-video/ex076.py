#Programa que tem uma tupla com uma lista de produtos e seus preços, o programa cria uma lista organizando os dados
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90) #Tupla com o nome dos produtos e seus preços
print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)
for c in range(0, len(lista)):
    if c % 2 == 0: #Os produtos estão na posição par da tupla, então serão organizados a esquerda
        print(f'{lista[c]:.<30}', end='') 
    else: #Os preços estão na posição ímpar e serão organizados a esquerda
        print(f'R$ {lista[c]:>6.2f}')