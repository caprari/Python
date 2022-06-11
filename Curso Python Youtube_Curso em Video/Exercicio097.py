def cabecalho(titulo):
    print(40*'=')
    print(titulo)
    from datetime import datetime
    print(datetime.today().strftime('%d/%m/%Y'))
    print(datetime.today().strftime('%H:%M:%S'))
    print(40*'=')


def controle():
    print('Formatação do Texto')
    print(40*'-')
    texto = str(input('Digite o texto: '))
    tamanho = len(texto) + 4
    print('=' * tamanho)
    print(texto.center(tamanho))
    print('=' * tamanho)


cabecalho('Início do Programa')
controle()
cabecalho('Fim do Programa')

