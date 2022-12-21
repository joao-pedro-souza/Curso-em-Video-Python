lista = list()
pares = list()
impares = list()

for x in range(7):
    num = int(input(f'Digite o {x+1}º número: '))
    lista.append(num)
for x in lista:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')