print(29*'=')
print('* Início do Programa')
print('* Cadastro de Alunos e Situação')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
print()

aluno = {}
lista_alunos = []

while True:
        aluno['nome'] = str(input('Digite o nome do aluno: '))
        aluno['média'] = float(input('Digite a média final: '))

        if aluno['média'] >= 7:
                aluno['situação'] = 'Aprovado'
        elif aluno['média'] < 5:
                aluno['situação'] = 'Reprovado'
        else:
                aluno['situação'] = 'Em Recuperação'

        lista_alunos.append(aluno.copy())
        print('Cadastro incluido na lista!')

        sair = str(input('Quer Continuar? [S/N]: '))
        print()
        if sair.upper() in 'N':
                break

print(lista_alunos)

print('Segue situação dos alunos cadastrados:')
for a in lista_alunos:
        for n in a.values():
                print(' - ', n, end='\n')
        print()

print(29*'=')
print('* Fim do Programa')
from datetime import datetime
print(datetime.today().strftime('* %d/%m/%Y'))
print(datetime.today().strftime('* %H:%M:%S'))
print(29*'=')
