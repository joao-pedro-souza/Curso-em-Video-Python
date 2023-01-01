#Programa que lê km rodados e dias alugados e calcula o custo de um aluguel
km = float(input('Quantos km rodados? '))
dias = int(input('Quantos dias alugados? '))
aluguel = (dias*60)+(km*0.15)
print(f'O total a pagar é R$ {aluguel}')