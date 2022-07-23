from random import randint

valor_aleatorio = randint(0, 10)
acertou = False
while acertou == False:
    chute = int(input('Chute um número de 0 a 10: '))
    if chute < valor_aleatorio:
        print('Você errou. Chute menor que número gerado')
    elif chute > valor_aleatorio:
        print('Você errou. Chute maior que valor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print('Você acertou')

