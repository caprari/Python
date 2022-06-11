('='*29)
print('* Média deIdade')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

total = 4
soma = 0

for loop in range(0, total):
    nome = str(input('Informe o nome: '))
    idade = int(input('Informe a idade: '))
    soma = soma + idade
    sexo = str(input('Informe o sexo (M para Masculino e F para Feminino: '))
    print(' ')

media = soma / total
print('A média de idade é de {:.2f} anos!'.format(media))

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
