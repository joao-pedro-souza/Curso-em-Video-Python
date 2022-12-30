#Programa que lê altura e largura de uma parede e diz quantos litros de tinta serão necessários para pintark
h = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
a = h * l
print(f'A area da parede é {a} metros², serão necessários {a/2} litros de tinta para pintar')  
