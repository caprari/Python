('='*29)
print('* Início do Programa')
print('* Somatória apenas de números pares')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
n4 = int(input('Informe o quarto número: '))
n5 = int(input('Informe o quinto número: '))
n6 = int(input('Informe o sexto número: '))

r1 = n1 % 2
r2 = n2 % 2
r3 = n3 % 2
r4 = n4 % 2
r5 = n5 % 2
r6 = n6 % 2

soma = 0

if r1 == 0:
    soma = soma + n1
if r2 == 0:
    soma = soma + n2
if r3 == 0:
    soma = soma + n3
if r4 == 0:
    soma = soma + n4
if r5 == 0:
    soma = soma + n5
if r6 == 0:
    soma = soma + n6

print(soma)

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
