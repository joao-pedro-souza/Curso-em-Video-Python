preço = float(input('Digite o preço do produto: '))
print('''Forma de pagamento:
[0] para pagar à vista no dinheiro
[1] para pagar à vista no cartão
[2] ou mais para o número de vezes que deseja parcelar''')
resposta = int(input('Qual a forma de pagamento? '))
if resposta == 0:
    preço = preço - (preço*10/100)
    print('Você pagou à vista no dinheiro')
elif resposta == 1:
    preço = preço - (preço*5/100)
    print('Você pagou à vista no cartão')
elif resposta == 2:
    print(f'Você parcelou em 2 vezes de {preço/2}')
elif resposta >= 3:
    preço = preço + (preço*20/100)
    print(f'Você parcelou o produto em {resposta} vezes de {(preço+preço*20/100)/resposta}')
print(f'O preço final do produto é R${preço}')