from datetime import time

print(40*'=')
print('* Início do Programa')
print('* Jogador de Futebol')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(40*'=')
print()

jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do Jogador: '))
total_jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, total_jogos):
    partidas.append(int(input(f'    Quantos gols {jogador["nome"]} marcou na partida {c+1}: ')))

jogador['gols'] = partidas[:]
jogador["total"] = sum(partidas)
print()

print(30*'=-')
print(f'O jogador {jogador["nome"]} fez um total de {jogador["total"]} de gols nas {total_jogos} partidas.')
print(30*'=-')

for k, v in jogador.items():
    print(f'O campo {k} tem um total de {v}.')
print(30*'=-')

print(f'O jogador {jogador["nome"]} jogou {len(partidas)} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'    - Na partida {i+1}, fez {v} gols.')

print(f'O jogador {jogador["nome"]} fez um total de {jogador["total"]} gols.')
print(30*'=-')

print()
print(40*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(40*'=')
