import random
valor = random.randint(1,10)
acertou = False
tentativas = 0
while acertou == False:
    chute = int(input('chute um número de 1 a 10: '))
    tentativas +=1
    if chute == valor:
        acertou = True
print(f'Você acertou em {tentativas} tentativas ')

