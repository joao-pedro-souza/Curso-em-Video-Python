s = 0
soma = 0
for c in range(1,500):
    if c%3==0 and c%2==1:
        s += 1
        soma += c
print(f'A soma dos {s} múltiplos de 3 é {soma}')