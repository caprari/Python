print(29*'=')
print('* Início do Programa')
print('* Cadastro de Pessoas')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print()

pessoa = {}
lista_pessoas = []
total = 0
soma_idade = 0
media = 0

while True:
        pessoa['nome'] = str(input('Nome: '))

        while True:
                pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]

                if pessoa['sexo'] in 'MF':
                        break
                print('ERRO! Digite apenas M ou F.')

        pessoa['idade'] = int(input('Idade: '))

        lista_pessoas.append(pessoa.copy())
        print('Cadastro incluido na lista!')
        total = total + 1

        soma_idade = soma_idade + pessoa['idade']

        while True:
                sair = str(input('Quer Continuar? [S/N]: ')).upper()[0]
                if sair in 'SN':
                        break
                print('ERRO! Digite apenas S ou N.')
        if sair == 'N':
                break

        print()

media = soma_idade / len(lista_pessoas)

print()
print(40*'=-')
print(f'Foram cadastradas {total} pessoas.')
print(f'Foram cadastradas {len(lista_pessoas)} pessoas.')
print(f'A soma da idade das {len(lista_pessoas)} pessoas cadastradas é {soma_idade}.')
print(f'A média de idade das {len(lista_pessoas)} pessoas é {media:.0f}.')

print(f'A lista de mulheres cadastradas é a seguinte: ', end='')
for c in lista_pessoas:
        if c['sexo'] in 'F':
                print(f'{c["nome"]} ', end='')
print()

print(f'A lista de homens cadastrados é a seguinte: ', end='')
for c in lista_pessoas:
        if c['sexo'] in 'M':
                print(f'{c["nome"]} ', end='')
print()

print(f'A lista de pessoas acima da média de idade é a seguinte: ', end='')
for c in lista_pessoas:
        if c['idade'] > media:
                print(f'{c["nome"]} ', end='')
print()

print(40*'=-')


print()
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
