from Curso_Python_Youtube_Curso_em_Video_ex115.lib.interface import *
from Curso_Python_Youtube_Curso_em_Video_ex115.lib.arquivo import *
from time import sleep

# arquivo = 'cadastro.csv'
arquivo = 'cadastro.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)


while True:
    resposta = menu(['Listar pessoas cadastradas', 'Cadastrar nova pessoa', 'Deletar pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        peso = float(input('Peso: '))
        altura = float(input('Altura: '))
        buscarCodigo(arquivo)
        print(codigo)
        codigo = codigo + 1
        calculoIMC(peso, altura)
        cadastrarPessoa(codigo, arquivo, nome, idade, peso, altura)
    elif resposta == 3:
        cabecalho('Deletar pessoa!')
        break
    elif resposta == 4:
        cabecalho('Saindo do Sistema!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

