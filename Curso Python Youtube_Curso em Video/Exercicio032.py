print('='*29)
print('* Início do Programa')
print('* Categoria de Natação')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

print(' ')
print('Informe o seu nome e data de nascimento')
nome = str(input('Nome: '))
dia = str(input('Dia de Nascimento: '))
mes = str(input('Mês de Nascimento: '))
ano = str(input('Ano de Nascimento: '))

data_nascimento = int(ano + mes + dia)
data_atual = int(datetime.today().strftime('%Y%m%d'))
print(data_nascimento)
print(data_atual)
#qtde_ano = abs()

anos = data_atual - data_nascimento
print('Você está com {:.2f}'.format(anos))



#if imc < 16:
#    print("Magreza grave")
#elif imc < 17:
#    print("Magreza moderada")
#elif imc < 18.5:
#    print("Magreza leve")
#elif imc < 25:
#    print("Saudável")
#elif imc < 30:
#    print("Sobrepeso")
#elif imc < 35:
#    print("Obesidade Grau I")
#elif imc < 40:
#    print("Obesidade Grau II (severa)")
#else:
#    print("Obesidade Grau III (mórbida)")
#

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
