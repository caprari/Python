print('='*29)
print('* Início do Programa')
print('* Raiz Quadrada Função Math')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

# import datetime - importa todos os dados do modulo datetime
# from datetime import date - importa apenas a data do modulo
# from math import ceil as arrendoda_cima

from math import sqrt, floor, ceil

numero = int(input('Digite um número: '))
raiz = sqrt(numero)
print(' ')
print('A raíz quadrada de {} é igual a {:.2f}'.format(numero, raiz))
print('A raíz quadrada de {} arredondada pra cima é {}'.format(numero, ceil(raiz)))
print('A raíz quadrada de {} arredondada pra baixo é {}'.format(numero, floor(raiz)))

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
