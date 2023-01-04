#Programa que lê o nome de uma cidade e mostra em letras maiúsculas, se a cidade começa com "Santo", mostra True na tela
cidade = input('Em qual cidade você nasceu? ')
cidade = cidade.upper()
print(f'Você nasceu em Santo...? {"SANTO" in cidade}')