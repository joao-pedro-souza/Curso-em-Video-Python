#Programa que tem uma tupla com várias palavras, e depois mostra quais são as vogais
palavras = ('Mesa', 'Camisa', 'Parede', 'Porta', 'Computador', 'Programação')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou': #Verifica se a palavra tem vogais
            print(f'{letra}', end=' ') #Se tiver será exibida na tela