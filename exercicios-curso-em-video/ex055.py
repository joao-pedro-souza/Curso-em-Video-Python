maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}º pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    elif menor == 0:
        menor = maior
print(f'A pessoa mais pesada tem {maior}kg, e a pessoa mais leve tem {menor}kg')