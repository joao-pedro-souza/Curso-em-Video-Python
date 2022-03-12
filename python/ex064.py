soma = para = digitados = 0
while para != 999:
    para = int(input('Digite um número [999 para parar]: '))
    if para != 999:
        soma += para
        digitados += 1
print(f'Foram digitados {digitados} números e a soma entre eles é {soma}')