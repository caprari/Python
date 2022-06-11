import random


def cabecalho(titulo):
    print(40*'=')
    print(titulo)
    from datetime import datetime
    print(datetime.today().strftime('%d/%m/%Y'))
    print(datetime.today().strftime('%H:%M:%S'))
    print(40*'=')


def aleatorio(lista):
    print(40*'-')
    from random import randint
    print('Os 5 números sorteados foram:', end=' ')
    for cont in range(0, 5):
        numero = random.randint(1, 10)
        lista.append(numero)
        print(f'{numero}', end=' ')
    print()
    print(40*'-')


def somaPar(lista):
    soma_par = 0
    soma_impar = 0
    for valor in lista:
        if valor % 2 == 0:
            soma_par = soma_par + valor
        else:
            soma_impar = soma_impar + valor
    print(f'A soma dos números pares é: {soma_par}.')
    print(f'A soma dos números impares é: {soma_impar}.')


cabecalho('Início do Programa')
numeros = []
aleatorio(numeros)
somaPar(numeros)
cabecalho('Fim do Programa')
