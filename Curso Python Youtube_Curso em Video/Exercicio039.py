('='*29)
print('* Início do Programa')
print('* Qtde de Números Pares e Impares')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

par = 0
impar = 0
soma_par = 0
soma_impar = 0

for loop in range(0, 5):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        par = par + 1
        soma_par = soma_par + numero
    else:
        impar = impar + 1
        soma_impar = soma_impar + numero

print(' ')
print('Você digitou {} número(s) par(es) e {} número(s) ímpar(es).'.format(par, impar))
print('A soma dos números pares é {}.'.format(soma_par))
print('A soma dos números impares é {}.'.format(soma_impar))

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
