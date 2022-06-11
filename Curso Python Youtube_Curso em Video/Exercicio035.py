('='*29)
print('* Início do Programa')
print('* Tabuada')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

numero = int(input('Informe um número para saber a tabuada: '))
for loop in range(1, 11):
    tabuada = numero * loop
    print('{} x {} = {}'.format(numero, loop, tabuada))

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
