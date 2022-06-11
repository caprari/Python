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


def leiaint():
    """
    -> Informar apenas um número inteiro
    :return: Número informado.
    """
    while True:
        num = str(input('Digite um número inteiro: '))
        if num.isnumeric():
            print(f'O número informado foi o {num}.')
            break
        print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')
        #Cor Vermelha: \033[1;31m     \033[m


cabecalho('Início do Programa')
print()
leiaint()
print()
cabecalho('Fim do Programa')
