#Programa que lê algo pelo teclado e mostra variás informações sobre o que foi digitado
a = input('Digite algo: ') #Pede que o usúario digite algo
print('O tipo primitivo desse valor é ', type(a)) #Mostra o tipo primitivo do que foi digitado 
print(f'Só tem espaços? \33[31;4m{a.isspace()}\33[m') #Mostra se só foram digitados espaços
print(f'É um número? \33[32;4m{a.isnumeric()}\33[m') #Mostra se úm número foi digitado
print(f'É alfabético? \33[33;4m{a.isalpha()}\33[m') #Mostra se o que foi digitado é alfabético
print(f'É alfanumérico? \33[34;4m{a.isalnum()}\33[m') #Mostra se o que foi digitado é alfanumérico
print(f'Está em maiúsculo? \33[35;4m{a.isupper()}\33[m') #Mostra se todas as letras estão em maiúsculo
print(f'Está em minúsculo? \33[36;4m{a.islower()}\33[m') #Mostra se todas as letras estão em minúsculo
print(f'Está capitalizado? \33[37;4m{a.istitle()}\33[m') #Mostra se a primeira letra das palavras está em maiúsculo
    