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


def notas(*n, sit=False):
    """

    :param n: Notas
    :param sit: >= 7 = BOA, >= 5 e <7 = REGULAR, <5 = RUIM
    :return: Dicionário com as Notas
    """
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)

    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'REGULAR'
        else:
            r['Situação'] = 'RUIM'
    return r
    print(r)


cabecalho('Início do Programa')
print()
resp = notas(2, 4, 3, 7, sit=False)
print(resp)
print()
cabecalho('Fim do Programa')
