from math import degrees, sin, tan, cos, radians
angûlo = int(input('Digite o ângulo: '))
print(f'O cosseno de {angûlo} é {cos(radians(angûlo)):.2f}')
print(f'O seno de {angûlo} é {sin(radians(angûlo)):.2f}')
print(f'A tangente de {angûlo} é {tan(radians(angûlo)):.2f}')