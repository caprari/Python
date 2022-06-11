import random

print(29*'=')
print('* Início do Programa')
print('* Criação de Lista')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print(' ')

valores = list()
valores.append(random.randint(1, 10))
valores.append(random.randint(1, 10))
valores.append(random.randint(1, 10))

for cont in range(0, 3):
    valores.append(int(input('Digite um número: ')))

valores.sort() #order

for c, v in enumerate(valores):
    print(f'O número {v} está na posição {c} da lista!')

print('')
print(valores)


print(' ')
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
