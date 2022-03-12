soma_de_pares = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}º número: '))
    if n%2==0:
        soma_de_pares += n
print(f'A soma de pares é {soma_de_pares}')