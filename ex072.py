#Programa que tem uma tupla com números escritos por extenso de 0 até 20, o programa lê um número de 0 a 20 pelo teclado e o mostra por extenso
n = 23
número = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte') #Tupla com os números por extenso
while n < 0 or n > 20:
    n = int(input('Digite um número entre 0 e 20: ')) #Lê um número entre 0 e 20
    if n < 0 or n > 20: #Se o valor digitado não estiver entre 0 e 20 será exibida a mensagem 'Tente novamente.'
        print('Tente novamente.')
    else: #Se o valor estiver entre 0 e 20 a estrutura while será encerrada
        break
print(f'Você digitou o número {número[n]}.') #Vai usar o número digitado para mostrar sua posição na tupla, mostrando o número escrito por extenso