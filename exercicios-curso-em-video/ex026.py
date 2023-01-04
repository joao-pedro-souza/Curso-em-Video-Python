#Programa que lê uma frase e mostra quantas vezes a letra A aparece, e em qual posição apareceu pela primeira e pela última vez
frase = input('Digite uma frase: ').strip()
print(f'A letra A aparece {frase.upper().count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.upper().find("A")+1}')
print(f'A letra A aparece pela última vez na posição {frase.upper().rfind("A")+1}')