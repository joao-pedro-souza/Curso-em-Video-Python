#Programa que lê um ângulo e mostra seno, cosseno e tangente
from math import degrees, sin, tan, cos, radians
angulo = int(input('Digite o ângulo: '))
print(f'O cosseno de {angulo} é {cos(radians(angulo)):.2f}')
print(f'O seno de {angulo} é {sin(radians(angulo)):.2f}')
print(f'A tangente de {angulo} é {tan(radians(angulo)):.2f}')
