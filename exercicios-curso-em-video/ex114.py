#Programa que tenta acessar o site Pudim e mostra se conseguiu ou não
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')