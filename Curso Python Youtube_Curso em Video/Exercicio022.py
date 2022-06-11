print('='*29)
print('* Início do Programa')
print('* Nome Completo   ')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

nome = str(input('Informe seu Nome Completo: '))
print('Nome em Maisculo:', nome.upper())
print('Nome em Minusculo:', nome.lower())
print('Quantidade de Caracteres informados:', len(nome))


print('Nome:', nome)


print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
