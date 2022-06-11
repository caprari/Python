print(29*'=')
print('* Início do Programa')
print('* Jogo de Dados')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print()

import random
import time

numero = []
sorteados = []

print('Valores Sorteados:')
for c in range(1, 5):
        numero.append(random.randint(1, 20))
        print(f'        O jogador {c} foi sorteado com o número {numero}.')
        sorteados.append(numero[:])
        numero.clear()
        time.sleep(1)

sorteados.sort()

print()
print('Ranking dos Jogadores:')
print(sorteados)

print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
