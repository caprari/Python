import uteis

num = int(input('Digite um número para saber o fatorial: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {uteis.dobro(num)}.')
print(f'O triplo de {num} é {uteis.triplo(num)}.')

# def cabecalho(titulo):
#     print(40*'=')
#     print(titulo)
#     from datetime import datetime
#     print(datetime.today().strftime('%d/%m/%Y'))
#     print(datetime.today().strftime('%H:%M:%S'))
#     print(40*'=')
#
#
# def parOuImpar(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def resultado():
#     if parOuImpar(num):
#         print(f'O número informado {num} é Par!')
#     else:
#         print(f'O número informado {num} é Impar!')
#
#
# cabecalho('Inicio do Programa')
# num = int(input('Digite um número: '))
# resultado()
# print()
#
# num = int(input('Digite um número: '))
# resultado()
# print()
#
# cabecalho('Fim do Programa')
# print()


#import random
#numero = []
#numero = random.sample(range(1, 7), 6)
#numero.sort()
#print(numero)

#from openpyxl import Workbook
#
#wb = Workbook()
#
#planilha = wb.worksheets[0]
#
#planilha['A1'] = 'banana'
#planilha['A2'] = 'pera'
#
#wb.save(r'C:\Users\Marcelo\PycharmProjects\pythonProject_inicio\Meuarquivo.xlsx')
#
#dados = 'Marcelo', 39, '1.75', '76.2'
#print(f'o {dados[0]} está com {dados[1]} anos, com {dados[2]} de altura e pesa {dados[3]}.')
#print(dados)

#contagem = int(input('Informe um número para saber a tabuada: '))
#import time
#for loop in range(10, 0, -1):
#    print(loop)
#    time.sleep(1)
#print('0')



#numero = int(input('Informe um número para saber a tabuada: '))
#for loop in range(1, 11):
#    tabuada = numero * loop
#    print('{} * {} = {}.'.format(numero, loop, tabuada))
#print('Fim!')

#numero = random.randint(1, 100)
#print('Número Aleatório gerado:', numero)


#frase = '  Curso em video Python  '
#print(frase[0:5])
#print(frase[:5])
#print(frase[6:])
#print(frase[0::2])
#print(len(frase))
#print(frase.count('o'))
#print(frase.count('o', 0, 14))
#print(frase.find('Cursos'))
#frase = frase.replace('Curso', 'Android')
#print(frase)
#print(frase.replace('Curso', 'Android'))
#
#print(frase.upper())
#print(frase.lower())
#print(frase.capitalize())
#print(frase.title())
#print(frase.strip())
#print(frase.rstrip())
#print(frase.lstrip())
#print(frase.split())
#print('-'.join(frase))



