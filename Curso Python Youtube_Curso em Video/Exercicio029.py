print('='*29)
print('* Início do Programa')
print('* Preço da Passagem')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

distancia = float(input('Informe a distância em KM para saber o valor da passagem: '))
print(' ')

ate_200 = 0.50
acima_200 = 0.45
valor_ate_200 = distancia * ate_200
valor_acima_200 = distancia * acima_200

if distancia <= 200:
    print('O valor da passagem para {} KM é R$ {:.2f}.'.format(distancia, valor_ate_200))
else:
    print('O valor da passagem para {} KM é R$ {:.2f}.'.format(distancia, valor_acima_200))

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
