# Criar o jogo Jokenpo
print('[ 1 ] PEDRA'
'[ 2 ] PAPEL' \
'[ 3 ] TESOURA')
import random
pc = random.randint(1,3)
jogador = int(input('Digite um número para jogar: '))
from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if pc == 1 and jogador == 2:
    print('PC jogou Pedra. Jogador Vence! ')
elif pc == 1 and jogador == 3:
    print('PC jogou Pedra. PC vence! ')
elif pc == 2 and jogador == 1:
    print('PC jogou Papel. PC vence!')
elif pc == 2 and jogador == 3:
    print('PC jogou papel. JOgador vence!')
elif pc == 3 and jogador == 1:
    print('PC jogou Tesoura. Jogador vence!')
elif pc == 3 and jogador == 2:
    print('PC jogou Tesoura. PC vence! ')
else:
    print('Vocês empataram!')