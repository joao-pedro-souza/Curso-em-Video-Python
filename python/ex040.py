n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
nota = (n1+n2) / 2
print('-'*15)
print(f'NOTA: {nota}')
if nota >= 7:
    print(f'STATUS: \33[32mAPROVADO\33[m')
elif nota < 5:
    print(f'STATUS: \33[31mREPROVADO\33[m')
else:
    print('STATUS: \33[36mRECUPERAÇÃO\33[m')