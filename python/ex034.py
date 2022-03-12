salário = float(input('Digite o seu sálario: R$'))
if salário >= 1250:
    print(f'Você teve um aumento de 10%, seu novo sálario é de R${salário+(salário*10/100)}')
else:
    print(f'Você teve um aumento de 15%, seu novo salário é de R${salário+(salário*15/100)}')