import forca
import AluraJogo

print("Qual jogo deseja jogar? Digite a opção escolhida. ")
escolha_do_jogo = int(input("(1) - FORCA  (2) - ADVINHAÇÃO: "))

if escolha_do_jogo == 1:
        forca.jogar()
elif escolha_do_jogo == 2:
        AluraJogo.jogar()
else:
    print("Opção Inválida. Tente novamente")

