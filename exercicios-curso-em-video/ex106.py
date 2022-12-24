def escreva(txt):
    print('~'*(len(txt)+4))
    print(f'  {txt}  ')
    print('~'*(len(txt)+4))


while True:
    escreva('SISTEMA DE AJUDA PyHELP')
    comando = input('Função ou Biblioteca: ')
    if comando.lower() == 'fim':
        escreva('ATÉ LOGO')
        break
    else:
        escreva(f'Acessando o manual do comando {comando}')
        help(comando)