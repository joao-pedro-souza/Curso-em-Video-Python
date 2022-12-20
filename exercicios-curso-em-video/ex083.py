#Programa que verifica se uma expressão matemática é válida ou não
lista = list(input('Digite uma expressão matemática: '))
x = 0
for item in lista:
    if item == '(':
        x += 1
    if item == ')':
        x -= 1
if x == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')