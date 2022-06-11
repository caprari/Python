def cabecalho(titulo):
    """
    -> Função cabeçalho
    :param titulo: Nome do Programa
    :return: Nome do Programa
    """
    print(40*'=')
    print(titulo)
    from datetime import datetime
    print(datetime.today().strftime('%d/%m/%Y'))
    print(datetime.today().strftime('%H:%M:%S'))
    print(40*'=')

c = ('\033[m',      # 0 -Sem Cores
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m'
     )


def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('=' * tam)
    print(f'{msg}')
    print('=' * tam)
    print(c[0], end='')


cabecalho('Início do Programa')
print()
comando = ''
while True:
    titulo('Sistema de Ajuda PyCharm', 2)
    comando = str(input('Digite um função ou biblioteca (Fim para Sair): '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

print()
cabecalho('Fim do Programa')
