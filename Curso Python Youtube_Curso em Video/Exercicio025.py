print('='*29)
print('* Início do Programa')
print('* Aluno Aprovado, Reprovado ou Recuperação')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*29)
print(' ')

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
nota4 = float(input('Digite a 4ª nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(' ')
print('A média das notas foi {:.2f}.'.format(media))

if media >= 7.0:
    print('Parabéns, você foi aprovado!')
elif media < 5.0:
    print('Infelizmente você foi reprovado!')
else:
    print('Você está em recuperação!')


print(' ')
print('='*26)
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print('='*26)
