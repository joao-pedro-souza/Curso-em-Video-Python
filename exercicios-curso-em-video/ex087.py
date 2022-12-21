#Programa que cria uma matriz 3 por 3 e faz a soma dos números pares, a soma dos valores da terceira coluna e verifica o maior número da segunda linha
matriz = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
somapar = 0
somacol3 = 0
maiorlin2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o número da posição {l}, {c}: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somacol3 += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maiorlin2:
                maiorlin2 = matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print(f'A soma de números pares é {somapar}')
print(f'A soma dos números da terceira coluna é de {somacol3}')
print(f'O maior valor da segunda linha é {maiorlin2}')