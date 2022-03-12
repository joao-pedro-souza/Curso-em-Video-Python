from random import randint
pc = randint(0,10) #Faz o computador escolher um número aleatório entre 0 e 10
usuário = 11 
tentativas = 0 #Calcula o número de tentativas
while pc != usuário: #Enquanto a resposta do usuário for diferente do pc essa estrutura vai se repitir
    usuário = int(input('Chute um número: ')) #Variavel que guarda o chute do usúario
    if pc > usuário:
        print('Mais... Tente novamente.') #Se o chute do usuário for maior do que o número, o pc vai dar essa dica
        tentativas += 1 #Faz a variavel do número de tentativas aumentar
    elif pc < usuário:
        print('Menos... Tente novamente.') #Se o chute do usuário for menor, o pc vai dar essa dica
        tentativas += 1
print(f'Eu pensei no número {pc}, você precisou de {tentativas} tentativas para acertar') #Mostra qual foi o número que o pc gerou e quantas tentativas o usuário precisou para acertar