print('='*29)
print('* Início do Programa        *')
print('* Conversão de Moeda        *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y                *'))
print(datetime.today().strftime('* %H:%M:%S                  *'))
print('='*29)

print(' ')

valor_reais = float(input('Digite o valor em Reais: '))

# Ordem de Calculo de Valores
# ()
# **
# * / // %
# + -

valor_dolares = valor_reais / 3.27

print(' ')
print('Pode ser comprado {:.2f}'.format(valor_dolares), 'dolares')


print(' ')
print('='*26)
print('* Fim do Programa        *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y             *'))
print(datetime.today().strftime('* %H:%M:%S               *'))
print('='*26)
