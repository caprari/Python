('='*29)
print('* Início do Programa')
print('* Menu na Tela')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print(' ')

print('Menu de Opções:')
print('[1] para Somar')
print('[2] para Multiplicar')
print('[3] para Descobrir o maior valor')
print('[4] para Informar novos números')
print('[5] para Sair do Programa')

opcao = int(input('Informe a opção: '))

while opcao != 5:
    if opcao == 1:
        soma = n1 + n2
        print('A soma dos números {} e {} é {}.'.format(n1, n2, soma))
        opcao = int(input('Informe a opção: '))
    if opcao == 2:
        multiplica = n1 * n2
        print('A multiplicação dos números {} e {} é {}.'.format(n1, n2, multiplica))
        opcao = int(input('Informe a opção: '))
    if opcao == 3:
        if n1 == n2:
            print('Os números {} e {} são iguais.'.format(n1, n2))
        elif n1 > n2:
            print('O primeiro número {} é maior que o segundo número {}.'.format(n1, n2))
        else:
            print('O primeiro número {} é menor que o segundo número {}.'.format(n1, n2))
        opcao = int(input('Informe a opção: '))
    if opcao == 4:
        n1 = int(input('Digite o primeiro número novamente: '))
        n2 = int(input('Digite o segundo número novamente: '))
        opcao = int(input('Informe a opção: '))

print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
