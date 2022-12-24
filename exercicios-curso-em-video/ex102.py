#Programa que tem uma função fatorial() que recebe dois parâmetros: o número que será calculado e o parâmetro opcional show, que indica se o processo de cálculo será mostrado ou não
def fatorial(n, show=False):
    f = 1
    for c in range (n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f
    
print(fatorial(8, True))