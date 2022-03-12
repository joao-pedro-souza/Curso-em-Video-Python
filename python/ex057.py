r = input('Qual seu sexo [M/F]? ').strip().upper()[0]
while r not in 'MmFf':
    r = input('Dados inválidos, digite novamente: ').strip().upper()[0]
print(f'Sexo {r} registrado com sucesso!')