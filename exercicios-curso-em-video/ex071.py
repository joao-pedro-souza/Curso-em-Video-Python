#Programa que pede ao usuário um valor a ser sacado e mostrará quantas cédulas de R$50, R$20, R$10, R$1 serão sacadas
n = int(input('Digite o valor a ser sacado: R$')) #Recebe o valor que vai ser sacado
cédula = 50 #Valor das cédulas, começa com R$50
total = 0 #Variavel que guarda o total de cédulas que foram sacadas
while True:
    if n >= cédula: #Se o valor for maior do que o valor da cédula, as cédulas serão sacadas
        n -= cédula
        total += 1 #Vai aumentar o total de cédulas sacadas
    else:
        if total > 0: #Se alguma cédula for sacada, será exibida quantas cédulas foram e o valor delas
            print(f'Foram sacadas {total} cédulas de R${cédula}.')
        if cédula == 50: #Vai diminuir o valor das cédulas até que o valor chegue a R$0
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total = 0
        if n == 0: #Quando o valor chegar a R$0 o programa será encerrado
            break
