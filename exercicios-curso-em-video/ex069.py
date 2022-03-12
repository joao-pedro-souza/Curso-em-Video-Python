#Programa que lê a idade e sexo de várias pessoas, até que o usuário escolher não continuar, ao final o programa mostra quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos.
maiores = homens = mulheres = 0
while True:
    idade = int(input('Idade: ')) #Lê a idade
    sexo = input('Sexo: [M/F] ').strip().upper()[0] #Lê o sexo
    if idade >= 18: #Se a idade for maior que 18, a variavel 'maiores' vai aumentar em 1
        maiores += 1
    if sexo == 'M' and idade > 0: #Se o sexo for masculino a variavel 'homens' vai aumentar em 1
        homens += 1
    if sexo == 'F' and idade < 18: #Se o sexo for feminino e a idade menor que 18, a variavel 'mulheres' vai aumentar em 1
        mulheres += 1
    continuar = input('Quer continuar? [S/N] ').strip().upper() #Pergunta se o usuário quer continuar
    if continuar == 'N': #Se a resposta for não, a estrutura while é encerrada
        break
print(f'Foram registradas {maiores} pessoas maiores de idade.') #Mostra quantas pessoas tem mais de 18 anos
print(f'Foram registrados {homens} homens.') #Mostra quantos homens foram cadastrados
print(f'Foram registradas {mulheres} mulheres menores de idade.') #Mostra quantas mulheres com menos de 18 anos foram cadastradas