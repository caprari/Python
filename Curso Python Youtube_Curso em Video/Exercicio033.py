('='*29)
print('* Início do Programa')
print('* Jogo: Jokenpô')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

import random
informado = str(input('Informe PA para Papel, TE para Tesoura e PE para Pedra: '))
print(' ')

jokenpo = random.choice(['pedra', 'papel', 'tesoura'])
print('Escolha PC:', jokenpo)
print('Escolha Usuário: {}'.format(informado))
print(' ')

if informado == 'PA' and jokenpo == 'pedra':
    print('Você ganhou pois papel embrulha {}.'.format(jokenpo))
elif informado == 'TE' and jokenpo == 'papel':
    print('Você ganhou pois tesoura corta {}.'.format(jokenpo))
elif informado == 'PE' and jokenpo == 'tesoura':
    print('Você ganhou pois pedra quebra {}'.format(jokenpo))
elif informado == 'PA' and jokenpo == 'tesoura':
    print('Você perdeu pois papel é cortado pela {}.'.format(jokenpo))
elif informado == 'TE' and jokenpo == 'pedra':
    print('Você perdeu pois tesoura é quebrada pela {}.'.format(jokenpo))
elif informado == 'PE' and jokenpo == 'papel':
    print('Você perdeu pois pedra é embrulhada pelo {}.'.format(jokenpo))
else:
    print('Empate')



print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
