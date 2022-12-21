matriz = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
somapar = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o número da posição {l}, {c}: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print(f'A soma de números pares é {somapar}')