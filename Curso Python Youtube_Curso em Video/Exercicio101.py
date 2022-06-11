def cabecalho(titulo):
    print(40*'=')
    print(titulo)
    from datetime import datetime
    print(datetime.today().strftime('%d/%m/%Y'))
    print(datetime.today().strftime('%H:%M:%S'))
    print(40*'=')


def voto():
    from datetime import datetime
    idade2 = datetime.now()
    idade3 = idade2.year
    ano = int(input('Digite o seu ano de nascimento: '))
    elegivel = idade3 - ano
    print(elegivel)

    if elegivel < 16:
        print(f'Com {elegivel} anos, você não pode votar!')
    elif elegivel > 65:
        print(f'Com {elegivel} anos, você possui voto opcional!')
    elif elegivel == 16:
        print(f'Com {elegivel} anos, você possui voto opcional!')
    elif elegivel == 17:
        print(f'Com {elegivel} anos, você possui voto opcional!')
    else:
        print(f'Com {elegivel} anos, você é obrigado a votar!')


cabecalho('Início do Programa')
voto()
cabecalho('Fim do Programa')
