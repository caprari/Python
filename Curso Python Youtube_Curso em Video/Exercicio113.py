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
        try:
            num = int(input('Digite um número inteiro: '))
            break
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')
            #Cor Vermelha: \033[1;31m     \033[m

    while True:
        try:
            real = float(input('Digite um número decimal: '))
            break
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número decimal válido!\033[m')
            #Cor Vermelha: \033[1;32m     \033[m

    print(f'O número inteiro foi o {num} e o número decial foi o {real}.')


cabecalho('Início do Programa')
print()

leiaint()

print()
cabecalho('Fim do Programa')
