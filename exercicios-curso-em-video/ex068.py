#Jogo Par ou Ímpar, o jogo continuará até que o usuário perca
from random import randint
vitórias = 0 #Guarda o número de vitórias do usuário
while True: #Repetira essa estrutura até que o usuário perca
    pc = randint(0,10) #O computador vai gerar um número aleatório entre 0 e 10
    par_ou_ímpar = input('Par ou ímpar? [P/I] ').strip().upper()[0] #Vai perguntar se o usuário vai escolher par ou ímpar, desconsiderando espaços, em maiusculo e apenas a primeira letra
    valor = int(input('Digite um número: ')) #Vai pedir um número ao usuário
    soma = valor + pc #Vai somar o número que o computador escolheu com o do usuário
    if soma % 2 == 0: #Se o resto dessa soma for igual a 0, o número é par
        resultado = 'PAR' #Resultado recebe o valor 'PAR'
    else: #Se o número não for par o resultado vai receber o valor 'ÍMPAR'
        resultado = 'ÍMPAR'
    print(f'Você jogou {valor} e o computador {pc}. O total de {soma} deu {resultado}.') #Mostra os valores escolhidos e o resultado 
    if par_ou_ímpar == 'P' and resultado == 'PAR' or par_ou_ímpar == 'I' and resultado == 'ÍMPAR': #Verifica se a escolha do usuário foi igual ao resultado
        print('VOCÊ GANHOU!') #Se o usuário ganhar, vai receber uma mensagem de vitória e seu número de vitórias vai aumentar
        vitórias += 1 
    else:
        print('VOCÊ PERDEU') #Se o usuário perder receberá uma mensagem de derrota e o programa será finalizado
        break
print(f'Você conseguiu {vitórias} vitórias consecutivas.') #Ao final do programa o usuário será informado quantas vitórias ele obteve