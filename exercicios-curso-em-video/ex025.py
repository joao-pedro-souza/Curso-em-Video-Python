#Programa que lê um nome completo, se o nome tem Silva mostra True na tela
nome = input('Qual seu nome completo? ')
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')