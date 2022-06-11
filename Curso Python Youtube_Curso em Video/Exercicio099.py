def cabecalho(titulo):
    print(40*'=')
    print(titulo)
    from datetime import datetime
    print(datetime.today().strftime('%d/%m/%Y'))
    print(datetime.today().strftime('%H:%M:%S'))
    print(40*'=')


def maior(* num):
    print(40*'-')
    contador = 0
    maior = 0
    soma = 0
    print('Análise dos Números informados:')
    while True:
        num = int(input(f'Informe um número: '))
        soma = soma + num
        if contador == 0:
            maior = num
        elif num > maior:
            maior = num
        contador = contador + 1

        while True:
            sair = str(input('Quer Continuar? [S/N]: ')).upper()[0]
            if sair in 'SN':
                break
            print('ERRO! Digite apenas S ou N.')
        if sair == 'N':
            break

    print(f'A soma dos números informados é {soma}.')
    print(f'O maior valor informe foi o {maior}.')


cabecalho('Início do Programa')

maior()

cabecalho('Fim do Programa')
