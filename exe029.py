#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite
vel = int(input('Digite sua velocidade: '))
multa = (vel - 80) * 7
if vel <= 80:
    print ('Ótima viagem, dirija com segurança!')
else:
    print ('Voê foi multado. O valor da multa é de {}'.format(multa))

