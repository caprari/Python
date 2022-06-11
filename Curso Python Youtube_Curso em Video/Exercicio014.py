print('='*29)
print('* Início do Programa')
print('* Cálculo de Tinta')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)

print(' ')

altura = int(input('Digite a altura da parede: '))
largura = int(input('Digite a largura da parede: '))

# Ordem de Calculo de Valores
# ()
# **
# * / // %
# + -

area_total = altura * largura
litro_metro = 2
litro_total = area_total * litro_metro

print(' ')
print('A área total de pintura são {}'.format(area_total), 'metros')
print('Para essa área, serão necessários {}'.format(litro_total), 'litros de tinta')



print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
