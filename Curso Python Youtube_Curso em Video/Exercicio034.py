('='*29)
print('* Início do Programa')
print('* Contagem Regressiva')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

import time

informado = int(input('Informe o número de início para a Contagem Regressiva: '))
print(' ')

for loop in range(informado, 0, -1):
    print(loop)
    time.sleep(1)
print('0')

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
