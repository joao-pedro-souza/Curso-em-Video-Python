import moeda

n = float(input('Digite o preço: R$'))
print(f'A metade de {n} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {n} é {moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(n, 13))}')