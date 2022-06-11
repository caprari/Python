print(29*'=')
print('* Início do Programa')
print('* Jogo de Par ou Impar')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print(' ')

import random

print('Vamos Jogar Par ou Ímpar')
print(' ')

while True:
    numero_aleatorio = random.randint(1, 30)
    numero = int(input('Digite um número: '))
    escolha = str(input('Par ou Ímpar? [P/I]: '))
    escolha = escolha.upper()
    soma = numero + numero_aleatorio
    resto = soma % 2
    print(f'Você informou {numero} e o computador {numero_aleatorio}. Total de {soma}.')
    if resto == 0 and escolha == 'P':
        print('Deu Par, você ganhou!')
        break
    elif resto == 0 and escolha == 'I':
        print('Deu Ímpar, você perdeu!')
    elif resto != 0 and escolha == 'P':
        print('Deu Ímpar, você perdeu!')
    else:
        print('Deu Par, você ganhou!')
        break

print(' ')
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
