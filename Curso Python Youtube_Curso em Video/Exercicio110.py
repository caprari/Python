import moeda


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


cabecalho('Início do Programa')
print()

num = str(input('Digite o valor R$: '))

print()
print('-'*40)
print('RESUMO DO VALOR'.center(40))
print('-'*40)
print(f'Preço informado:      R$ {num:.2f}')
print(f'Dobro do preço:       R$ {moeda.dobro(num):.2f}')
print(f'Metade do preço:      R$ {moeda.metade(num):.2f}')
print(f'20% de aumento:       R$ {moeda.aumentar(num, 20):.2f}')
print(f'15% de desconto:      R$ {moeda.diminuir(num, 15):.2f}')
print('-'*40)

print()
cabecalho('Fim do Programa')
