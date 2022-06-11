print('='*29)
print('* Início do Programa')
print('* Tabuada')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)

numero = 0

while True:
    print(' ')
    print('-'*65)
    numero = int(input('Gostaria de ver a tabuada de qual valor (Informe 0 para sair): '))
    print('-'*65)
    if numero == 0:
        break
    for loop in range(1, 11):
        tabuada = numero * loop
        print(f'{numero} x {loop} = {tabuada}')

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
