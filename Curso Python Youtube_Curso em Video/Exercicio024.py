print('='*29)
print('* Início do Programa')
print('* Informar Primeiro e Último Nome')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

nome = str(input('Informe seu nome completo: '))
nome = nome.split()
print(' ')
print('Seu nome completo é: {}'.format(nome))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))

#print('Unidade: {}'.format(unidade))
#print('Dezena: {}'.format(dezena))
#print('Centena: {}'.format(centena))
#print('Milhar: {}'.format(milhar))

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
