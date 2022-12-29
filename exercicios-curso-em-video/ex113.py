def leiaInt(msg):
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Você digitou um número inválido.\033[m')
        else:
            return num

def leiaFloat(msg):
    while True:

        try:
            num = float(input('Digite um número real: '))
        except (KeyboardInterrupt):
            print('\033[0;31mO Usuário preferiu não digitar esse número\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Você digitou um número inválido.\033[m')
        else:
            return num

i = leiaInt('Digite um número: ')
f = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {i} e o número real {f}')