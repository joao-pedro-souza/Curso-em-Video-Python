d = float(input('Qual a distância da viagem? '))
if d<= 200:
    print('A viagem vai custar R$0.50 por km')
    print(f'Preço: R${d*0.5}')
else:
    print('A viagem vai custar R$0.45 por km')
    print(f'Preço: R${d*0.45}')