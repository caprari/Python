print('='*29)
print('* Início do Programa')
print('* Aumento de Salário')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)

print(' ')

salario_atual = float(input('Digite o salário atual em R$: '))
percentual_aumento = float(input('Digite o percentual de aumento: '))
aumento = salario_atual * percentual_aumento / 100
salario_novo = salario_atual + aumento

print(' ')
print('O seu novo salário será de R$ {:.2f}'.format(salario_novo))

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
