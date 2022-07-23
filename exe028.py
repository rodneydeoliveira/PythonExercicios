#Escreva um programa que faça o computador “pensar” em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.
import random
valor = random.randint(0,5)
chute = int(input('Digite um número entre 0 e 5: '))
if chute == valor:
    print ('Você acertou!')
else:
    print ('Você errou, eu ganhei. O número que eu pensei foi {}'.format(valor))