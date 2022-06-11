print('='*29)
print('* Início do Programa        *')
print('* Média de 4 Notas          *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y                *'))
print(datetime.today().strftime('* %H:%M:%S                  *'))
print('='*29)

print(' ')

nota1 = int(input('Digite a 1ª nota: '))
nota2 = int(input('Digite a 2ª nota: '))
nota3 = int(input('Digite a 3ª nota: '))
nota4 = int(input('Digite a 4ª nota: '))

# Ordem de Calculo de Valores
# ()
# **
# * / // %
# + -

media = (nota1 + nota2 + nota3 + nota4) / 4

print(' ')
print('A média das notas é {:.2f}'.format(media))
print(' ')


print(' ')
print('='*26)
print('* Fim do Programa        *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y             *'))
print(datetime.today().strftime('* %H:%M:%S               *'))
print('='*26)
