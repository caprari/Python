print('='*29)
print('* Início do Programa')
print('* Solicitação de Financiamento')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

print('Vamos para simular o valor do financiamento, insira alguns dados por favor.')
valor_casa = float(input('Qual o valor da casa/apartamento? '))
salario = float(input('Qual o seu salário atual? '))
prazo = int(input('Qual o prazo (em anos) para pagamento? '))
print(' ')

prestacao = valor_casa / (prazo * 12)
max_parcela = salario * 33 / 100

if prestacao > max_parcela:
    print('O empréstimo foi negativado pois a parcela mensal excede o percentual máximo de 30% do seu salário!')
    print('A parcela mensal foi calculada em R$ {:.2f} e o valor máximo é de R$ {:.2f}.'.format(prestacao, max_parcela))
    exit()
else:
    print('Parabéns, o seu empréstimo foi pré-aprovado!')
    print('A parcela mensal será de R$ {:.2f}.'.format(prestacao))

aprova = str(input('Se está DE ACORDO com o valor da parcela, digite S, se não, digite N: '))

if aprova == 'S' or 's' or 'SIM' or 'Sim' or 'sim':
    print('Obrigado, o empréstimo será liberado em até 5 dias úteis na sua conta!')
    print(' ')
    print('Segue resumo:')
    print('Valor do empréstimo: R$ {:.2f}.'.format(valor_casa))
    print('Prazo de pagamento (em anos): {}.'.format(prazo))
    print('Valor previsto da parcela: R$ {:.2f}.'.format(prestacao))
else:
    print('Obrigado, sua solicitação de empréstimo foi cancelada!')


print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
