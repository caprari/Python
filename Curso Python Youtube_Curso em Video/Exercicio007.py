print('**************************')
print('* Início do Programa     *')
print('* Acerte o Filme         *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y             *'))
print(datetime.today().strftime('* %H:%M:%S               *'))
print('**************************')

print(' ')
print('Por favor, digite alguns dados para prosseguirmos')
print(' ')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
filme = 'Sonic'
print(' ')
print(nome, ', agora você tem 3 tentativas para acertar o nome do filme!')

total_de_tentativas = 3
tentativa = 1

while(tentativa <= total_de_tentativas):
    print(' ')
    print('Tentativa', tentativa, 'de', total_de_tentativas)
    if (tentativa == 3):
        print('Última tentativa, pense bem antes de responder!')

    chute_filme = input(str('Digite o filme: '))

    if (chute_filme == filme):
        print('Parabéns, você acertou!')
        tentativa = 4
    else:
        if (tentativa != 3):
            print('Você errou, tente novamente!')

    tentativa = tentativa + 1

print(' ')
print('**************************')
print('* Fim do Programa        *')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y             *'))
print(datetime.today().strftime('* %H:%M:%S               *'))
print('**************************')
