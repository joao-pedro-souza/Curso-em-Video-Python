def voto(i):
    from datetime import date
    i =  date.today().year - i
    if i < 16:
        return f'Com {i} anos: Não Vota'
    elif i > 17 and i < 65:
        return f'Com {i} anos: Voto Obrigatório'
    else:
        return f'Com {i} anos: Voto Opcional'

idade = int(input('Em que ano você nasceu? '))
print(voto(idade))