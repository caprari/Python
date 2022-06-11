print('='*29)
print('* Início do Programa')
print('* Ordem de Apresentação')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

import random

lista_alunos = ['Marcelo', 'Luciana', 'Henrique', 'Arthur']
random.shuffle(lista_alunos)
print('Ordem de Apresentação:', lista_alunos)


print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
