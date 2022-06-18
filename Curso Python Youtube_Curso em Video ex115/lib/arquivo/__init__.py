from ex115.lib.interface import *
from ex115.lib.arquivo import *

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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<33}{dado[1]:3>} anos')

        print(a.read())
    finally:
        a.close()


def cadastrarPessoa(arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(arquivo, 'a')
    except:
        print('Erro ao abrir arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao cadastrar no arquivo!')
        else:
            print(f'{nome} cadastrado(a) com sucesso!')
            a.close()



