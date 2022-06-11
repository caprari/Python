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
print(f'    O dobro de {num} é {moeda.dobro(num)}.')
print(f'    A metade de {num} é {moeda.metade(num)}.')
print(f'    Aumento 10% de {num} temos {num+moeda.aumentar(num)}.')
print(f'    Dimunuindo 15% de {num} temos {num-moeda.diminuir(num)}.')

print()
cabecalho('Fim do Programa')
