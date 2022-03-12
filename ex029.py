v = int(input('Digite a velocidade do carro: '))
if v>80:
    print('Você excedeu o limite de velocidade de 80km/h e foi multado')
    print(f'O valor da multa é de R${(v-80)*7}')