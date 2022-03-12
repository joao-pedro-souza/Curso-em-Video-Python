while True:
    nome = input('Digite seu nome: ')
    if len(nome)>3:
        break
    else:
        print('O nome precisa ter mais de 3 caracteres')
while True:
    idade = int(input('Digite sua idade: '))
    if idade >= 0 and idade <= 150:
        break
    else:
        print('Idade inválida, tente novamente')
while True:
    salário = float(input('Digite seu sálario: R$'))
    if salário >= 0:
        break
    else:
        print('Salário inválido, tente novamente.')
while True:
    sexo = input('Digite seu sexo: [M/F]').strip().upper()
    if sexo in 'MF':
        break
    else:
        print('Sexo inválido. Tente novamente.')
while True:
    print('''Digite seu estado civil
[S]Solteiro
[C]Casado
[V]Viúvo
[D]Divorciado''')
    estado = input('Estado Civil: ').strip().upper()
    if estado in 'SCVD':
        break
    else:
        print('Estado Civil invalido. Tente novamente.')
print(f'''Seus dados:
Nome: {nome}
Idade: {idade}
Sexo: {sexo}
Salário: {salário}
Estado Civil: {estado}''')
        
        
        