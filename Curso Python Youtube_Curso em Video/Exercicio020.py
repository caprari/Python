print('='*29)
print('* Início do Programa')
print('* Escolher um aluno aleatório')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

import random

lista_alunos = ['Marcelo', 'Luciana', 'Henrique', 'Arthur']
random.shuffle(lista_alunos)
print('Aluno Sorteado:', random.choice(lista_alunos))
print(random.sample(lista_alunos, 3))

#print(random.randint(aluno1, aluno2, aluno3, aluno4))


print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
