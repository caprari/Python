def cabecalho(titulo):
    print(40*'=')
    print(titulo)
    from datetime import datetime
    print(datetime.today().strftime('%d/%m/%Y'))
    print(datetime.today().strftime('%H:%M:%S'))
    print(40*'=')


def controle():
    print('Controle de Terrenos')
    print(40*'-')
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    total = largura * comprimento
    print(f'A área do terreno {largura:.2f} x {comprimento:.2f} é de {total:.2f} m².')


cabecalho('Início do Programa')
controle()


cabecalho('Fim do Programa')

