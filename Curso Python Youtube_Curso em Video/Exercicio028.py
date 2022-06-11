print('='*29)
print('* Início do Programa')
print('* Número Par ou Impar')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

numero = int(input('Informe um número para saber se é PAR ou IMPAR: '))
print(' ')

numero = numero % 2
# comando % = resto da divisao

if numero == 0:
    print('Número informado é PAR!')
else:
    print('Número informado é IMPAR!')

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
