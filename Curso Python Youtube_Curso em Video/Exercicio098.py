from time import sleep

def cabecalho(titulo):
    print(40*'=')
    print(titulo)
    from datetime import datetime
    print(datetime.today().strftime('%d/%m/%Y'))
    print(datetime.today().strftime('%H:%M:%S'))
    print(40*'=')


def contagem():
    print(40*'-')
    print('Contagem de 1 até 10 de 1 em 1')
    for numero in range(1, 11):
        print(numero, end=' ')
        sleep(0.5)
    print()
    print(40*'-')
    print('Contagem de 10 até 0 de 2 em 2')
    for numero2 in range(0, 11, 2).__reversed__():
        print(numero2, end=' ')
        sleep(0.5)
    print()
    print(40*'-')
    print('Agora informe os números para personalizar a contagem!')
    inicio = int(input('Início: '))
    fim    = int(input('Fim:    '))
    passo  = int(input('Passo:  '))
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio >= fim:
        for numero3 in range(inicio, fim, passo):
            print(numero3, end=' ')
            sleep(0.5)
        print()
    else:
        for numero3 in range(inicio, fim, passo).__reversed__():
            print(numero3, end=' ')
            sleep(0.5)
        print()


cabecalho('Início do Programa')

contagem()

cabecalho('Fim do Programa')
