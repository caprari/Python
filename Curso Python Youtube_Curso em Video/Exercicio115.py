def menu():
    print('-'*40)
    print('Menu Principal'.center(40))
    print('-'*40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do Sistema')
    print('-'*40)


def opcao(opcao):
    while True:
        try:
            # opcao = int(input('Sua opção: '))
            if opcao in (1, 2, 3):
                break
            print('\033[1;31mERRO! Informe apenas 1, 2 ou 3 como opção.\033[m ')
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Opção inválida, informe a opção corretamente.\033[m ')

menu()
opcao = (int(input('Sua opção: ')))
