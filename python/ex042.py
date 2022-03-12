l1 = float(input('Primeiro Lado: '))
l2 = float(input('Segundo Lado: '))
l3 = float(input('Terceiro Lado: '))
if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('Não podem formar um triângulo') 
else: 
    print('Podem formar um triângulo')
    if l1 == l2 and l2 == l3:
        print('Triângulo equilátero.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triângulo isósceles.')
    else:
        print('Triângulo escaleno')