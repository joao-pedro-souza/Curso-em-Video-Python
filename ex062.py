n1 = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
cont = 0
fim = 10
while cont < fim:
    print(f'{n1} > ' , end='')
    n1 += razão
    cont += 1
    if cont == fim:
        print('PAUSA')
        fim = fim + int(input('\nQuantos termos a mais você quer mostar? '))
print(f'{cont} termos foram mostrados.')
print('FIM')
    


    
        
