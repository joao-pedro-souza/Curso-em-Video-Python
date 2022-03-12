from distutils.command.clean import clean


a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print(f'Só tem espaços? \33[31;4m{a.isspace()}\33[m')
print(f'É um número? \33[32;4m{a.isnumeric()}\33[m')
print(f'É alfabético? \33[33;4m{a.isalpha()}\33[m')
print(f'É alfanumérico? \33[34;4m{a.isalnum()}\33[m')
print(f'Está em maiúsculo? \33[35;4m{a.isupper()}\33[m')
print(f'Está em minúsculo? \33[36;4m{a.islower()}\33[m')
print(f'Está capitalizado? \33[37;4m{a.istitle()}\33[m')
    