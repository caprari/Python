from datetime import datetime

def criar_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor


def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print(f'O saldo da conta {(conta["numero"])} é R$ {(conta["saldo"])}.')
    print(f'O titular da conta {(conta["numero"])} é o {(conta["titular"])}.')
    data_acesso = datetime.today().strftime('%d/%m/%Y')
    hora_acesso = datetime.today().strftime('%H:%M:%S')
    data_hora_consulta = data_acesso + ' às ' + hora_acesso
    print(f'A consulta foi realizada em {data_hora_consulta}.')


conta = criar_conta(123, 'Marcelo', 77.10, 1000.00)
print(conta)
deposita(conta, 100.00)
print(conta)
saca(conta, 20.00)
print(conta)
extrato(conta)
