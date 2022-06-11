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
lista_numeros.sort(reverse=True)
print(f'Os números informados em ordem decrescente foi a seguinte: {lista_numeros}!')

if 5 in lista_numeros:
    print('O número 5 está na lista!')
else:
    print('O número 5 não consta na lista!')

print()
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
