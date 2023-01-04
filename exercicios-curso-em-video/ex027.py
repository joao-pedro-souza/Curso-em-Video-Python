#Programa que lê um nome completo, separa e mostra o primeiro e último nome
nome = input('Digite seu nome completo: ').strip()
d = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {d[0]}')
print(f'Seu último nome é {d[-1]}')