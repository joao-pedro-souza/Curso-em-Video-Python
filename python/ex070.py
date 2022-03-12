total = mil = barato = 0
nome_barato = '0'
while True:
    nome = input('Nome do Produto: ')
    preço = float(input('Preço: R$'))
    total += preço
    if barato == 0:
        barato = preço
        nome_barato = nome
    if preço < barato:
        barato = preço
        nome_barato = nome
    if preço > 1000:
        mil += 1
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print('Fim das compras.')
print(f'Total: R${total:.2f}')
print(f'Produtos que custam mais de R$1000: {mil}')
print(f'Produto mais barato: {nome_barato}')
print(f'Preço: {barato}')