#Programa que lê algo pelo teclado e mostra variás informações sobre o que foi digitado
a = input('Digite algo: ') #Pede que o usúario digite algo
print('O tipo primitivo desse valor é ', type(a)) #Mostra o tipo primitivo do que foi digitado 
print(f'Só tem espaços? {a.isspace()}') #Mostra se só foram digitados espaços
print(f'É um número? {a.isnumeric()}') #Mostra se úm número foi digitado
print(f'É alfabético?  {a.isalpha()}') #Mostra se o que foi digitado é alfabético
print(f'É alfanumérico? {a.isalnum()}') #Mostra se o que foi digitado é alfanumérico
print(f'Está em maiúsculo? {a.isupper()}') #Mostra se todas as letras estão em maiúsculo
print(f'Está em minúsculo? {a.islower()}') #Mostra se todas as letras estão em minúsculo
print(f'Está capitalizado? {a.istitle()}') #Mostra se a primeira letra das palavras está em maiúsculo
    