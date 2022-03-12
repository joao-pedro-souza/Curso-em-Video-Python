salário = float(input('Qual o seu salário? '))
casa = float(input('Qual o valor da casa? '))
anos = int(input('Em quantos anos vai pagar? '))

if casa/anos/12 > salário*30/100:
    print(f'A prestação vai custar R${casa/anos/12:.2f}. Empréstimo cancelado')
else:
    print(f'A prestação vai custar R${casa/anos/12:.2f}. Empréstimo aprovado')