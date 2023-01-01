#Programa que lê dois catetos e mostra a hipotenusa
from math import hypot
ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))
print('A hipotenusa é', hypot(ca, co))
