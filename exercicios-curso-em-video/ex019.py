#Programa que lê 4 nomes de alunos e bota em uma lista, depois sorteia um
from random import choice
aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')