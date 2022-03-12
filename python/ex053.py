frase = input('Digite a frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(f'{junto}')
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')