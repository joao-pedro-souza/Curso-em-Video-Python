#Programa que pede uma distância em metros e faz a conversão para centímetros, milímetros, decímetros, decâmetros, hectômetros e quilômetros
m = int(input('Qual é a distância em metros? '))
print(f'{m} metros equivalem à {m*100} centímetros, ou {m*1000} milímetros')
print(f'DM = {m*10}')
print(f'DAM = {m/10}')
print(f'HM = {m/100}')
print(f'KM = {m/1000}')