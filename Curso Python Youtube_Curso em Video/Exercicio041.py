('='*29)
print('* Início do Programa')
print('* Informe vários números')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

print('Obs: Digite 999 para terminar')
print(' ')
qtde = 0
numero = 0
soma = 0
multiplica = 0

while numero != 999:
    multiplica = soma * numero
    soma = soma + numero
    qtde = qtde + 1
    numero = int(input('Digite um número: '))

print(' ')
print('A soma dos {} números informados é {}.'.format(qtde - 1, soma))
print('A multiplicao dos {} números informados é {}.'.format(qtde - 1, multiplica))

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
