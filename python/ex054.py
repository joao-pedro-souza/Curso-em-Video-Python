maioridade = 0
from datetime import date
ano = date.today().year
for c in range(1,6):
    nasc = int(input('Ano de nascimento: '))
    if ano - nasc >= 21:
        maioridade += 1
print(f'A quantidade de maiores de idade é: {maioridade}')