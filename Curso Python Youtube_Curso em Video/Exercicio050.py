print(29*'=')
print('* Início do Programa')
print('* Lista dentro de lista ')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print(' ')

lista_dados = []
lista_concat = []
total = 0

while True:
    lista_dados.append(str(input('Digite seu nome: ')))
    lista_dados.append(float(input('Digite seu peso: ')))
    lista_concat.append(lista_dados[:])
    lista_dados.clear()
    total = total + 1

    sair = str(input('Quer Continuar? [S/N] '))
    if sair.upper() in 'N':
        break

print(' ')
for b in lista_concat:
    if b[1] > 30:
        print(f'{b[0]} pesa {b[1]} kgs e está acima do peso.')
    else:
        print(f'{b[0]} pesa {b[1]} kgs e está com peso normal')

print(f'Foram informados {total} pessoas.')


print(lista_concat)


print(' ')
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
