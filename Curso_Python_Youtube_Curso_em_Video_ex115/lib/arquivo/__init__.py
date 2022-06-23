from Curso_Python_Youtube_Curso_em_Video_ex115.lib.interface import *
from Curso_Python_Youtube_Curso_em_Video_ex115.lib.arquivo import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'w+')
        a.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro na leitura do arquivo')
    else:
        cabecalho('Pessoas Cadastradas')
        print('Codigo', 'Nome'.ljust(38), 'Idade', '  Peso', '  Altura', '  IMC')
        for linha in a:
            dado = linha.split(';')
            dado[5] = dado[5].replace('\n', '')
            print(f'{dado[0]}      {dado[1]:<42}{dado[2]:<3}  {dado[3]:<5}  {dado[4]:<5}    {dado[5]:>5}')

        print()
        cabecalho('Tabela de Referência de IMC')
        print('Abaixo de 16      - Magreza Grave\n'
              'Entre 16.1 e 16.9 - Magraza Moderada\n'
              'Entre 17.0 e 18.4 - Magraza Leve\n'
              'Entre 18.5 e 24.9 - Saudável\n'
              'Entre 25.0 e 29.9 - Sobrepeso\n'
              'Entre 30.0 e 34.9 - Obesidade Grau I\n'
              'Entre 35.0 e 39.9 - Obesidade Grau II (severa)\n'
              'Maior que 40.0    - Obesidade Grau III (mórbida)\n'
              )

        print()

        print(a.read())
    finally:
        a.close()


def cadastrarPessoa(codigo, arquivo, nome='Desconhecido', idade=0, peso=0, altura=0):

    imc2 = peso / altura**2
    imc = ('%.4f' % imc2)

    try:
        a = open(arquivo, 'a')
    except:
        print('Erro ao abrir arquivo!')
    else:
        try:
            a.write(f'{codigo};{nome};{idade};{peso};{altura};{imc}\n')
        except:
            print('Erro ao cadastrar no arquivo!')
        else:
            print(f'{nome} cadastrado(a) com sucesso!')
            a.close()


def calculoIMC(peso, altura):
    imc2 = peso / altura**2
    imc = ('%.1f' % imc2)
    return imc


def buscarCodigo(nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro na leitura do arquivo')
    else:
        return



