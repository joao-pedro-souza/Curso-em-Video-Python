#Programa que tem a função escreva(), que recebe um texto e mostra uma mensagem com tamanho adaptável
def escreva(txt):
    print('~'*(len(txt)+4))
    print(f'  {txt}  ')
    print('~'*(len(txt)+4))


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('Cev')