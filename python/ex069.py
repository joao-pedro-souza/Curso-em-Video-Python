maiores = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip().upper()
    if idade >= 18:
        maiores += 1
    if sexo == 'M' and idade > 0:
        homens += 1
    if sexo == 'F' and idade < 18:
        mulheres += 1
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
print(f'Foram registradas {maiores} pessoas maiores de idade.')
print(f'Foram registrados {homens} homens.')
print(f'Foram registradas {mulheres} mulheres menores de idade.')