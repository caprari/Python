import random

def jogar():

    cabecalho()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros = erros + 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    fim_do_jogo()


def cabecalho():
    print(20*'=-')
    print('Bem Vindo ao jogo da Forca!'.center(40))
    print('A palavra secreta é uma fruta!'.center(40))
    print('Boa sorte!'.center(40))
    print(20*'=-')


def carrega_palavra_secreta():

    # arquivo = open('frutas.txt', 'r')
    arquivo = open('desenhos.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        linha = linha.replace(' ', '')
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()[0]
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index = index + 1


def imprime_mensagem_vencedor(palavra_secreta):
    print(20*'=-')
    print("Parabéns, você ganhou!".center(40))
    print(f"A palavra era {palavra_secreta}!".center(40))
    print(20*'=-')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print(20*'=-')
    print('Puxa, você foi enforcado!'.center(40))
    print(f"A palavra era {palavra_secreta}!".center(40))
    print(20*'=-')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def fim_do_jogo():
    print(20*'=-')
    print('Fim do jogo!'.center(40))
    print(20*'=-')


if(__name__ == "__main__"):
    jogar()
