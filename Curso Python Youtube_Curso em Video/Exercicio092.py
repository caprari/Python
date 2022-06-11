from datetime import time

print(40*'=')
print('* Início do Programa')
print('* Cadastro de Trabalhadores')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(40*'=')
print()

nome = str(input('Nome: '))
ano_nascimento = int(input('Data de Nascimento: '))
carteira_trabalho = int(input('Carteira de Trabalho (0 não tem): '))
idade = datetime.now().year - ano_nascimento

if carteira_trabalho > 0:
    ano_contratacao = int(input('Ano de Contratação: '))
    salario = float(input('Salário: R$ '))

print()

print(30*'=-')
print(f'    - O nome informado foi {nome}.')
print(f'    - O ano de nascimento é {ano_nascimento}.')

if carteira_trabalho > 0:
    print(f'    - A CTPS é {carteira_trabalho}.')
    print(f'    - A contratação foi em {ano_contratacao}.')
    print(f'    - O salário atual é de R$ {salario}.')
    aposentadoria = idade + ((ano_contratacao + 35) - datetime.now().year)
    if idade >= aposentadoria:
        print(f'    - Você já deveria estar aposentado.')
    else:
        print(f'    - A sua aposentadoria será com {aposentadoria} anos.')

print(30*'=-')


print()
print(40*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(40*'=')
