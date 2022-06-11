def cabecalho(titulo):
    print(40*'=')
    print(titulo)
    from datetime import datetime
    print(datetime.today().strftime('%d/%m/%Y'))
    print(datetime.today().strftime('%H:%M:%S'))
    print(40*'=')


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial do número informado.
    """

    f = 1
    n = int(input('Informe um número para saber o fatorial: '))
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


cabecalho('Início do Programa')
print(fatorial(10, show=True))
help(fatorial)
cabecalho('Fim do Programa')
