n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
if n1>n2:
    print(f'{n1} é \33[36;4mmaior\33[m.')
elif n1==n2:
    print(f'{n1} e {n2} são \33[36;4miguais\33[m.')
else:
    print(f'{n2} é \33[36;4mmaior\33[m.')