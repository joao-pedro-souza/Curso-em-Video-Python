def leiaInt(msg):
    while True:
        num = str(input('Digite um número inteiro: ')).strip()
        try:
            return int(num)
            break
        except:
            print('\033[0;31mERRO! Você digitou um número inválido.\033[m')


def leiaFloat(msg):
    while True:
        num = str(input('Digite um número decimal: ')).strip().replace(',', '.')
        try:
            return float(num)
            break
        except:
            print('\033[0;31mERRO! Você digitou um número inválido.\033[m')


i = leiaInt('Digite um número: ')
print(f'Você digitou o número {i}')
f = leiaFloat('Digite um número decimal: ')
print(f'Você digitou o número {f}')
