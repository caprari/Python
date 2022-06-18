from Curso_Python_Youtube_Curso_em_Video_ex115.lib.interface import *
from Curso_Python_Youtube_Curso_em_Video_ex115.lib.arquivo import *
from time import sleep

# arquivo = 'cadastro.xls'
arquivo = 'cadastro.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Listar pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        peso = float(input('Peso: '))
        altura = float(input('Altura: '))
        calculoIMC(peso, altura)
        cadastrarPessoa(arquivo, nome, idade, peso, altura)
    elif resposta == 3:
        cabecalho('Saindo do Sistema!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

