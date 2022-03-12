print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
if l1 + l2 < l3 or l2 + l3 < l1 or l3 + l1 < l2:
    print(f'{l1}, {l2} e {l3} NÃO PODEM formar um triângulo.')
else:
    print(f'{l1}, {l2} e {l3} PODEM formar um triângulo.')