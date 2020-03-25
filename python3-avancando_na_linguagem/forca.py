import random

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    #CRIA UMA LISTA COM O ANDERLINE EM CADA LETRA DA PALAVRA SECRETA OBS: foi adcionado o parametro plavra_secreta para passar a variavel para a funcao
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0
  
    #ENQUANTO NAO ENFORCOU E NAO ACERTOU
    while(not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        #CASO A VARIAVEL ERROS FIQUE COM O VALOR 6, A VARIAVEL ENFORCOU SE TORNA TRUE E ASSIM O JOGO ACABA
        enforcou = erros == 7
        #DEIXA A VARIAVEL ACERTOU COMO TRUE CASO NÁO TENHA MAIS O ANDERLINE NA VARIAVEL LETRAS ACERTADAS
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

def imprime_mensagem_abertura():
    print("######################################")
    print("#####Bem vindo ao jogo de Forca!######")
    print("######################################")

def carrega_palavra_secreta():
    # LE O ARQUIVO PALAVRAS.TXT
    arquivo = open("palavras.txt", "r")
    # CRIA UMA LISTA PALAVRAS
    palavras = []

    # FOR PEGA CADA PALAVRA DO ARQUIVO E COLOCA NA LISTA PALAVRAS
    for linha in arquivo:
        # DEIXA O VALOR MAIUSCULO
        linha = linha.strip()
        # INSERE A PALAVRA NA LISTA
        palavras.append(linha)

    # FECHA O ARQUIVO
    arquivo.close()

    # ESCOLHE UM NUMERO ENTRE 0 ATE A QUANTIDADE DE PALAVRAS DENTRO DA LISTA
    numero = random.randrange(0, len(palavras))
    # DEFINE A PALAVA SECRETE DE ACODO COM UM INDICE DA LISTA PALAVRAS
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?")
    # REMOVE ESPACOS  E DEIXA MAIUSCULO
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    # FOR VERIFICA CADA CARACTER DA PALAVA E IRA MOSTRAR A LETRA DIGITADA TODAS AS VEZES QUE EXISTIR NA PALAVRA
    for letra in palavra_secreta:
        # IF VERIFICA O CHUTE COM CADA LETRA REPRESENTADA NO FOR COM A VARIAVEL LETRA
        if (chute == letra):
            # ADCIONA A LETRA ACERTA NA POSICAO CORRETA REPRESENTADA PELO INDEX
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
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
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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

if(__name__ == "__main__"):
    jogar()