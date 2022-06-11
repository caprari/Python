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

num = float(input('Digite o valor R$: '))
print(f'    O dobro de R$ {num:.2f} é R$ {moeda.dobro(num, formato=True):.2f}.')
print(f'    A metade de R$ {num:.2f} é R$ {moeda.metade(num, formato=True):.2f}.')
print(f'    Aumento 20% de R$ {num:.2f} temos R$ {moeda.aumentar(num, 20, formato=True):.2f}.')
print(f'    Dimunuindo 15% de R$ {num:.2f} temos R$ {moeda.diminuir(num, 15, formato=True):.2f}.')

print()
cabecalho('Fim do Programa')
