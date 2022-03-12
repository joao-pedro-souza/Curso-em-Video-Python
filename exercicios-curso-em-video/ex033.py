n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
maior = n1
if n2 > 1 and n2 > 3:
    maior = n2
if n3 > 1 and n3 > 2:
    maior = n3   
menor = n1
if n2 > 1 and n2 > 3:
    maior = n2
if n3 > 1 and n3 > 2:
    maior = n3
print(f'O maior é {maior}')
print(f'O menor é {menor}')