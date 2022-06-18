def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mERRO! Nenhuma opção foi informada!\033[m')
            return 0
        else:
            return num


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho(txt='MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;32m{c} - {item}\033[m')
        c = c + 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc


def cadastro(lista):
    nome = str(input('Informe o nome: '))
    idade = int(input('Informe a idade: '))

