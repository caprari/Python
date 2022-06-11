print(29*'=')
print('* Início do Programa')
print('* Criação de Lista')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print(' ')

lanche = ('carne', 'macarrão', 'sopa', 'churrasco') #tupla
comida = ['coxa', 'arroz', 'feijao', 'bife', 'batata frita'] #lista
print(lanche[1])
comida.append('teste4') #add no final
comida.insert(0, 'cookie') #add na posição 0
comida.remove('teste4') #remove com o nome informado
comida.pop(2) #remove na posicao informada
comida.pop() #remove o ultimo registro
if 'bife' in comida:
    comida.remove('bife')

comida.sort()
print(comida)

print(f'Essa list possui {len(comida)} comidas.')

print(' ')
print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
