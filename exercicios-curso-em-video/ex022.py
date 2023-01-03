#Programa que lê um nome completo e mostra ele em letras maiúsculas, minúsculas e o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
espaços = nome.count(' ')
print('Analisando seu nome...')
print('Seu nome todo em maiúsculo é', nome.upper())
print('Seu nome todo em minúsculo', nome.lower())
print(f'O seu nome tem {len(nome)-espaços} letras')
#print(f'O seu primeiro nome tem {len(dividido[0])} letras
print(f'O seu primeiro nome tem {nome.find(" ")}')
