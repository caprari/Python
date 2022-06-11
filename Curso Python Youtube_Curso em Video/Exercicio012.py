print('='*29)
print('* Início do Programa        *')
print('* Tabuada                   *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y                *'))
print(datetime.today().strftime('* %H:%M:%S                  *'))
print('='*29)

print(' ')

numero = int(input('Digite um número para exibir a tabuada: '))

# Ordem de Calculo de Valores
# ()
# **
# * / // %
# + -

print(' ')
print('A tabuada do', numero, 'é:')

termino = 10
inicio = 1

while(inicio <= termino):
    print(numero, '*', inicio, '=', (numero * inicio))
    inicio = inicio + 1

print(' ')
print('='*26)
print('* Fim do Programa        *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y             *'))
print(datetime.today().strftime('* %H:%M:%S               *'))
print('='*26)
