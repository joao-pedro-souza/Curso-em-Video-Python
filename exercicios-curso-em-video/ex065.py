digitados = maior = média = menor = resposta = 0
while resposta != 'N':
    n = int(input('Digite um número: '))
    média += n
    digitados += 1
    if digitados == 1:
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    resposta = input('Quer continuar [S/N]? ').strip().upper()
print(f'Você digitou {digitados} números e média foi {média/digitados}')
print(f'O maior número foi {maior} e o menor número foi {menor}')
    
