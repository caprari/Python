print('='*29)
print('* Início do Programa')
print('* Número Aleatório Função Randon')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

import random

numero = random.random()
print('Número Aleatório gerado:', numero)

numero = random.randint(1, 100)
print('Número Aleatório gerado:', numero)


print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
