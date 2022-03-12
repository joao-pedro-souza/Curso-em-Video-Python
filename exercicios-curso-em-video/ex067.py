#Programa que vai pedir ao usuário vários valores e vai mostrar suas tabuadas, o programa é encerrado quando o valor digitado for negativo
while True: #Vai repetir essa estrutura até que o número digitado seja negativo
    print('-'*40)
    n = int(input('Quer ver a tabuada de qual valor? ')) #Lê o número que o usuário digitar
    print('-'*40)
    if n < 0: #Interrompe o programa se o número for negativo
        break
    for c in range (1,11): #Vai repetir a estrutura abaixo 10 vezes, formando a tabuada do número digitado
        print(f'{n} x {c} = {n*c}')
print('PROGRAMA TABUADA ENCERRADO.')