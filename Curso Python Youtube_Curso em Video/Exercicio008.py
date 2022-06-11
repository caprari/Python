print('='*26)
print('* Início do Programa     *')
print('* Operação Aritmética    *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y             *'))
print(datetime.today().strftime('* %H:%M:%S               *'))
print('='*26)

print(' ')
nome = input('Por favor, digite seu nome para prosseguirmos: ')

print(' ')
print('Obrigado', nome, ', agora digite 2 números')

numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))

# Ordem de Calculo de Valores
# ()
# **
# * / // %
# + -

print(' ')
print('A soma dos números é {}'.format(numero1 + numero2))
print('A subtração dos números é {}'.format(numero1 - numero2))
print('A multiplicação dos números é {}'.format(numero1 * numero2))
print('A divisão dos números é {:.3f}'.format(numero1 / numero2))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
ponteciacao = numero1 ** numero2

print(' ')
print('A soma dos números é {}'.format(soma), end=' > ')
print('A subtração dos números é {}'.format(subtracao), end=' > ')
print('A multiplicação dos números é {}'.format(multiplicacao), end=' > ')
print('A divisão dos números é {:.3f}'.format(divisao))

print(' ')
print('='*26)
print('* Fim do Programa        *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y             *'))
print(datetime.today().strftime('* %H:%M:%S               *'))
print('='*26)
