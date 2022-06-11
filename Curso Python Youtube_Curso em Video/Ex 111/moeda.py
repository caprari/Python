def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def resumo(preco=0, taxaa=0, taxar=5):
    print('-'*30)
    print('Resumo do Valor'.center(30))
    print('-'*30)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preço:  \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, True)}')
    print('-'*30)

