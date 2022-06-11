
print(29*'=')
print('* Início do Programa')
print('* Cadastro de Filmes')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print()

cadastro_filme = {}
filmes = []

for c in range(0, 2):
        cadastro_filme['nome'] = str(input('Informe o nome do filme: '))
        cadastro_filme['ano_lançamento'] = int(input('Informe o ano de lançamento: '))
        cadastro_filme['gênero'] = str(input('Informe o gênero: '))
        filmes.append(cadastro_filme.copy())

for e in filmes:
        for n in e.values():
                print(n, end= ' ')
  #              print(f'O {n} foi lançado em {a} e é do gênero {g}.')
        print()

print()
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
