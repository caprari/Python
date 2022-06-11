print(29*'=')
print('* Início do Programa')
print('* Sorteio de Números da Mega Sena')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print()

import random
import time

numero_jogos = 0

numero_jogos = int(input('Quantos jogos deseja jogar? '))
print()

jogo_gerado = []
total = 1

while total <= numero_jogos:
        for c in range(0, 6):
            jogo_gerado.append(random.sample(range(1, 60), 1))
        jogo_gerado.sort()
        time.sleep(1)
        print(*jogo_gerado, sep = ',')
        print(f'Os números sorteados foram {jogo_gerado}.')
        jogo_gerado.clear()
        total = total + 1

print()
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
