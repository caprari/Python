print(29*'=')
print('* Início do Programa')
print('* Acerte o Número')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print(' ')

import random


numero_jogos = 0

numero_jogos = int(input('Quantos jogos d'))

print('Acerte o número aleatório de 1 a 10. Para desistir, digite 0!')
print(' ')

total_de_tentativas = 0
numero = 1

while numero != 0:
    numero_aleatorio = random.randint(1, 10)
    numero = int(input('Digite um número: '))
    if numero != 0:
        print(f'Número aleatório era {numero_aleatorio}.')
    total_de_tentativas = total_de_tentativas + 1
    if numero == numero_aleatorio:
        print('Parabéns, você acertou!')
        print(f'Foram necessárias {total_de_tentativas} tentativas!')
        numero = 0
    print(' ')

print(29*'=')
print('* Fim do Programa        *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
