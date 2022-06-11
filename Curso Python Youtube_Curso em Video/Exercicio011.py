print('='*29)
print('* Início do Programa        *')
print('* Conversão de Valores      *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y                *'))
print(datetime.today().strftime('* %H:%M:%S                  *'))
print('='*29)

print(' ')

metros = int(input('Digite a quantidade de metros: '))

# Ordem de Calculo de Valores
# ()
# **
# * / // %
# + -

kilometros = metros / 1000
centimetros = metros * 100
milimetros = metros * 1000
jardas = metros * 1.094
pes = metros * 3.281

print(' ')
print('O valor em kilometros é {:.3f}'.format(kilometros))
print('O valor em jardas é {:.3f}'.format(jardas))
print('O valor em pés é {:.3f}'.format(pes))
print('O valor em centímetros é {:.3f}'.format(centimetros))
print('O valor em milímetros é {:.3f}'.format(milimetros))
print(' ')


print(' ')
print('='*26)
print('* Fim do Programa        *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y             *'))
print(datetime.today().strftime('* %H:%M:%S               *'))
print('='*26)
