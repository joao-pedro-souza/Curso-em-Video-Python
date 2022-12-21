#Programa que cria uma matriz 3 por 3 com números digitados pelo usuário
matriz = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o número da posição {l}, {c}: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()