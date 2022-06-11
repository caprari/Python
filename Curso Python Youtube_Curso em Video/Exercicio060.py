import time

print(29*'=')
print('* Início do Programa')
print('* Jogo de Dados para 6 Jogadores')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print()

from random import randint
from time import sleep
from operator import itemgetter

jogo_dados = {'Marcelo': randint(1, 20),
              'Luciana': randint(1, 20),
              'Arthur': randint(1, 20),
              'Henrique': randint(1, 20),
              'Luverci': randint(1, 20),
              'Arlinda': randint(1, 20)}

ranking = []
print('Valores Sorteados:')

for k, v in jogo_dados.items():
        print(f'        {k} foi sorteado(a) com o número {v}.')
        time.sleep(1)

ranking = sorted(jogo_dados.items(), key=itemgetter(1), reverse=True)
print()
print('O Ranking dos jogadores sorteados é:')

for i, v in enumerate(ranking):
        print(f'        O {i+1}º lugar ficou com o(a) {v[0]} e número {v[1]}.')
        time.sleep(2)

print()
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
