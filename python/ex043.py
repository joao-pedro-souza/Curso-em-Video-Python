altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso/altura**2
print(f'IMC: \33[33m{imc:.1f}\33[m')
if imc < 18.5:
    print('STATUS: \33[31mAbaixo do peso\33[m')
elif imc >= 18.5 and imc <= 25:
    print('STATUS: \33[32mPeso Ideal\33[m')
elif imc > 25 and imc <= 30:
    print('STATUS: \33[31mSobrepeso\33[m')
elif imc > 30 and imc <= 40:
    print('STATUS: \33[31mObesidade\33[m')
else:
    print('STATUS: \33[31mObesidade mórbida\33[m')