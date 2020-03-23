import random

def jogar():

    print("######################################")
    print("Bem vindo ao jogo de advinhacao")
    print("######################################")

    #DEFINE O NUMERO SECRETO
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil?")

    #ARMAZENA A DIFICULDADE ESCOLHIDA PELO USUARIO E CONVERTE PARA INTEIRO
    nivel = int(input("Defina o nivel: "))

    #DEFINE O NUMERO DE TENTATIVAS DE ACORDO COM O NIVEL ESCOLHIDO
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #INICIA O JOGO DE ACORDO COM O NUMERO DE TENTATIVAS
    for rodada in range(1, total_de_tentativas + 1):
        #EXIBE AO USUARIO A RODADA E O NUMERO DE TENTATIVAS USANDO FOR E FORMAT
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        # CONVERTE O VALOR PARA INTEIRO
        chute = int(chute_str)

        #VERIFICA SE O VALOR DIGITADO ESTA ENTRE 0 A 100
        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100")
            continue

        #DEFINE VARIAVEIS PARA MELHOR COMPREENSAO DO CODIGO
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! O seu chute foi maior do que o numero secreto")
            elif(menor):
                print("Voce errou! O seu chute foi menor do que o numero secreto")
            #DEFINE O VALOR DA VARIAVEL PONTOS_PERDIDOS COMO HABISOLUTO, IGNORANDO NUMEROS NEGATIVOS
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo")

#EXECUTA A FUNCAO JOGAR APENAS SE FOR EXECUTADO  NO PROMPT
if(__name__ == "__main__"):
    jogar()