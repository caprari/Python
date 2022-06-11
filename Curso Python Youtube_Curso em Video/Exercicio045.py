print(29*'=')
print('* Início do Programa')
print('* Gravar em Tabela Excel')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print(' ')

from openpyxl import Workbook

wb = Workbook()

planilha = wb.worksheets[0]

nome = ' '

planilha['A1'] = 'NOME'
planilha['B1'] = 'IDADE'
planilha['C1'] = 'PESO'
planilha['D1'] = 'ALTURA'

planilha.title = 'Cadastro de Usuário'

planilha['A2'] = str(input('Digite seu nome: '))
planilha['B2'] = int(input('Digite sua idade: '))
planilha['C2'] = int(input('Digite seu peso: '))
planilha['D2'] = float(input('Digite sua altura: '))
wb.save(r'C:\Users\Marcelo\PycharmProjects\pythonProject_inicio\Cadastro de Usuários.xlsx')

print(' ')
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
