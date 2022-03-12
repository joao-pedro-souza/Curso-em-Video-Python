from random import choice
from time import sleep
jokenpô = ['papel', 'pedra', 'tesoura'] 
pc = choice(jokenpô)
print('-='*10)
print('      JOKENPÔ      ')
print('-='*10)
usuário = input('Vamos jogar jokenpô, digite o que vai escolher: ')
print('-='*10)
print('        JO         ')
sleep(0.5)
print('        KEN        ')
sleep(0.5)
print('        PO         ')
sleep(0.5)
print('-='*11)
print(f'Eu escolhi {pc}')
print(f'Você escolheu {usuário}')
print('-='*11)
if usuário.lower() == pc:
    print('        Empate        ')
elif usuário.lower() == 'pedra' and pc == 'papel':
    print('     Você perdeu!     ')
elif usuário.lower() == 'pedra' and pc == 'tesoura':
    print('     Você ganhou!     ')
elif usuário.lower() == 'tesoura' and pc == 'pedra':
    print('     Você perdeu!     ')
elif usuário.lower() == 'tesoura' and pc == 'papel':
    print('     Você ganhou!     ')
elif usuário.lower() == 'papel' and pc == 'tesoura':
    print('     Você perdeu!     ')
elif usuário.lower() == 'papel' and pc == 'pedra':
    print('     Você ganhou!     ')
else:
    print(f'{usuário} não é uma resposta válida! Use pedra, papel ou tesoura.')
print('-='*11)


