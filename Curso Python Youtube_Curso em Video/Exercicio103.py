def cabecalho(titulo):
    print(40*'=')
    print(titulo)
    from datetime import datetime
    print(datetime.today().strftime('%d/%m/%Y'))
    print(datetime.today().strftime('%H:%M:%S'))
    print(40*'=')


def ficha():
    jogador = str(input('Nome do jogador: '))
    if len(jogador) == 0:
        jogador = '<desconhecido>'

    try:
        gols = int(input(f'Quantos gol(s) {jogador} marcou? '))
    except:
        gols = 0

    try:
        jogos = int(input(f'Quantos jogo(s) {jogador} jogou? '))
    except:
        jogos = 0

    print(f'O jogador {jogador} fez {gols} gol(s) em {jogos} jogo(s) no campeonato!')
    if gols > 0 and jogos > 0:
        media = gols / jogos
        print(f'A média de gols por jogo foi de {media:.2f}!')


cabecalho('Início do Programa')
print()
ficha()
print()
cabecalho('Fim do Programa')
