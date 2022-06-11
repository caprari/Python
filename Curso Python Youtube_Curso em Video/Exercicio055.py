print(29*'=')
print('* Início do Programa')
print('* Matriz de Dimensão 3 x 3 ')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print()

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
soma_par = 0
soma_impar = 0
lista_par = []
lista_impar = []
soma_terc_coluna = 0
lista_terc_coluna = []
maior_valor_segun_linha = 0

for l in range(1, 4):
    for c in range(1, 4):
        matriz[l][c] = int(input(f'Digite um número para a posição {l} - {c}: '))
print(matriz)

for l in range(1, 4):
    for c in range(1, 4):
        print(f' [{matriz[l][c]:^5}] ', end=' ')

        if matriz[l][c] % 2 == 0:
            soma_par = soma_par + matriz[l][c]
            lista_par.append(matriz[l][c])
        else:
            soma_impar = soma_impar + matriz[l][c]
            lista_impar.append(matriz[l][c])

    print()

for l in range(1, 4):
    soma_terc_coluna = soma_terc_coluna + matriz[l][3]
    lista_terc_coluna.append(matriz[l][3])

for c in range(1, 4):
    if c == 0:
        maior_valor_segun_linha = matriz[1][c]
    elif matriz[1][c] > maior_valor_segun_linha:
        maior_valor_segun_linha = matriz[1][c]

print()
print(f'Os números pares informados foram: {lista_par}.')
lista_par.sort()
print(f'Os números em ordem crescente é: {lista_par}.')
lista_par.sort(reverse=True)
print(f'Os números em ordem decrescente é: {lista_par}.')
print(f'A soma dos números pares é {soma_par}.')

print()
print(f'Os números impares informados foram: {lista_impar}.')
lista_impar.sort()
print(f'Os números em ordem crescente é: {lista_impar}.')
lista_impar.sort(reverse=True)
print(f'Os números em ordem decrescente é: {lista_impar}.')
print(f'A soma dos números impares é {soma_impar}.')

print()
print(f'A lista dos números da 3ª coluna é: {lista_terc_coluna}.')
print(f'A soma dos números da 3ª coluna é: {soma_terc_coluna}.')

print()
print(f'O maior valor da coluna 1 é o {maior_valor_segun_linha}.')

print()
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
