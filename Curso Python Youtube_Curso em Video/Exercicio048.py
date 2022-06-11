import random

print(29*'=')
print('* Início do Programa')
print('* Ler 5 números em uma lista')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print(' ')

valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))
print(' ')

print(f'O maior valor informado foi o {max(valores)}')
print(f'O menor valor informado foi o {min(valores)}')
print(' ')

valores.sort()

for c, v in enumerate(valores):
    print(f'O número {v} está na posição {c} da lista!')

print(' ')
print(valores)

print(' ')
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
