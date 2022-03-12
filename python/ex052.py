for c in range(1,6):
    n = int(input(f'Digite o {c}º número: '))
    if n%1==0 and n%n==0:
        print('Esse número é primo')