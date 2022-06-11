print('='*29)
print('* Início do Programa')
print('* Desconto em Valor')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)

print(' ')

preco_atual = float(input('Digite o valor em R$: '))
percentual_desconto = float(input('Digite o percentual de desconto: '))
desconto = preco_atual * percentual_desconto / 100
preco_com_desconto = preco_atual - desconto

print(' ')
print('O valor com desconto é R$ {:.2f}'.format(preco_com_desconto))

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
