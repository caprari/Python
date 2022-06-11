print('='*29)
print('* Início do Programa        *')
print('* Cálculo de Números        *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y                *'))
print(datetime.today().strftime('* %H:%M:%S                  *'))
print('='*29)

print(' ')

numero1 = int(input('Digite o um número: '))

# Ordem de Calculo de Valores
# ()
# **
# * / // %
# + -

anterior = numero1 - 1
sucessor = numero1 + 1
dobro = numero1 * 2
triplo = numero1 * 3
raiz_quadrada = numero1 ** (1/2)

print(' ')
#print('O número anterior ao informado é {}'.format(anterior), end=' > ')
print('O número anterior ao informado é {}'.format(anterior))
print('O número sucessor ao informado é {}'.format(sucessor))
print('O dobro do número informado é {}'.format(dobro))
print('O triplo do número informado é {}'.format(triplo))
print('A raiz quadrada do número informado é {:.5f}'.format(raiz_quadrada))

print(' ')
print('='*26)
print('* Fim do Programa        *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y             *'))
print(datetime.today().strftime('* %H:%M:%S               *'))
print('='*26)
