print(29*'=')
print('* Início do Programa')
print('* Cadastro de Pessoas ')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print()

pessoas = []
lista_pessoas = []
maior = 0
menor = 0

while True:
    pessoas.append(str(input('Digite seu nome: ')))
    pessoas.append(float(input('Digite seu peso: ')))

    if len(pessoas) == 0:
        maior = pessoas[1]
        menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    lista_pessoas.append(pessoas[:])
    pessoas.clear()

    print('Cadastro incluido na lista!')

    sair = str(input('Quer Continuar? [S/N]: '))
    print()
    if sair.upper() in 'N':
        break

print()
print(f'Foram cadastradas {len(lista_pessoas)} pessoas!')
print(f'A lista de pessoas cadastradas é a seguinte {lista_pessoas}!')
print()
print(f'O maior peso informado foi de {maior} Kgs.')
print(f'O menor peso informado foi de {menor} Kgs.')


print()
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
