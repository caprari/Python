print(29*'=')
print('* Início do Programa')
print('* Lista de números ')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print()

lista_numeros = []
total = 0

while True:
    numero = int(input('Digite um número: '))

    if numero not in lista_numeros:
        lista_numeros.append(numero)
        total = total + 1
        print('Número adicionado na lista!')
    else:
        print('Número informado já existe na lista e não foi adicionado!')

    sair = str(input('Quer Continuar? [S/N]: '))
    print()
    if sair.upper() in 'N':
        break

print()
print(f'Foram informados {len(lista_numeros)} números!')
lista_numeros.sort()
print(f'Os números em ordem crescente é a seguinte: {lista_numeros}!')
lista_numeros.sort(reverse=True)
print(f'Os números em ordem decrescente é a seguinte: {lista_numeros}!')

pares = []
impares = []

for i, v in enumerate(lista_numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

if len(pares) == 1:
    print(f'O número par é o {pares}!')
elif len(pares) > 1:
    print(f'Os números pares são os seguintes {impares}!')
else:
    print('Não foram informados números pares!')

if len(impares) == 1:
    print(f'O número impar é o {pares}!')
elif len(impares) > 1:
    print(f'Os números impares são os seguintes {impares}!')
else:
    print('Não foram informados números impares!')

print()
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
