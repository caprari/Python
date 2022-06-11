from datetime import time

print(40*'=')
print('* Início do Programa')
print('* Jogador de Futebol')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(40*'=')
print()

time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    total_jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, total_jogos):
        partidas.append(int(input(f'    Quantos gols {jogador["nome"]} marcou na partida {c+1}: ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    print()

    while True:
        sair = str(input('Quer Continuar? [S/N]: ')).upper()[0]
        if sair in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if sair == 'N':
        break

print(40*'=-')
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print(40*'-')
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<13}', end='')
    print()
print(40*'=')

while True:
    buscar = int(input('Mostrar dados de qual jogador? [999 para Sair] '))
    if buscar == 999:
        break
    if buscar >= len(time):
        print(f'ERRO! Não tem jogador cadastrado com o código {buscar}!')
    else:
        print(f' --> Levantamento do Jogador {time[buscar]["nome"]}:')

        for i, g in enumerate(time[buscar]["gols"]):
            print(f'   - No jogo {i+1} fez {g} gols.')
    print(f'   - Total de {jogador["total"]} gols!')
    print(40*'=')


print()
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(40*'=')
