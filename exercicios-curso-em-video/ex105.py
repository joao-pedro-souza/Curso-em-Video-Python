#Programa que tem uma função notas() que pode receber notas de vários alunos, e retorna um dicionário com as seguintes informações: quantidade de notas, maior nota, menor nota, média da turma, situação(opcional)
def notas(*tupla, sit=False):
    dic = dict()
    total = 0
    maior = 0
    menor = 0
    soma = 0
    for n in tupla:
        total += 1
        soma += n
        if n > maior:
            maior = n
        if menor == 0:
            menor = n
        elif n < menor:
            menor = n
    dic['total'] = total
    dic['maior'] = maior
    dic['menor'] = menor
    dic['media'] = soma / total
    if sit:
        if soma / total >= 7:
            dic['situação'] = 'BOA'
        elif soma / total >= 5:
            dic['situação'] = 'RAZOÁVEL'
        elif soma / total < 5:
            dic['situação'] = 'RUIM'
    return dic


resp = notas(5, 10, 8, 7.5, sit=True)
print(resp)