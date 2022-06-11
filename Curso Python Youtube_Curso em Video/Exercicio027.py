print('='*29)
print('* Início do Programa')
print('* Ano informado é Bissexto')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

ano = int(input('Informe o ano para saber se é BISSEXTO ou não: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} É BISSEXTO!'.format(ano))
else:
    print('Ano {} NÃO É BISSEXTO!'.format(ano))


print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
