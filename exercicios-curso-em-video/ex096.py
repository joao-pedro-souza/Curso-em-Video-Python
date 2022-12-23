#Programa que tem uma função área(), que recebe largura e comprimento e mostra a área de um terreno
def área(l, c):
    print(f'A área de um terreno de {l}x{c} é de {l*c}m².')


print('Controle de Terrenos')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)