soma = digitados = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    digitados += 1
print(f'Foram digitados {digitados} números e a soma foi {soma}.')