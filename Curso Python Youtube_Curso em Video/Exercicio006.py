print('**************************')
print('* Início do Programa     *')
print('* Cálculo do IMC         *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y             *'))
print(datetime.today().strftime('* %H:%M:%S               *'))
print('**************************')

print(' ')
print('Informe o seu peso e altura atual')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura?: '))

imc = peso / altura**2

print(' ')
print("Seu IMC é: %.4f" % imc)

if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")


print('**************************')
print('* Fim do Programa        *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y             *'))
print(datetime.today().strftime('* %H:%M:%S               *'))
print('**************************')
