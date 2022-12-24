#Programa com uma função voto() que recebe o parâmetro ano de nascimento e retorna um valor literal que indica se uma pessoa tem não vota, tem voto opcional ou obrigatório
def voto(idade):
    from datetime import date
    idade =  date.today().year - idade
    if idade < 16:
        return f'Com {idade} anos: Não Vota'
    elif idade > 17 and idade < 65:
        return f'Com {idade} anos: Voto Obrigatório'
    else:
        return f'Com {idade} anos: Voto Opcional'

nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))