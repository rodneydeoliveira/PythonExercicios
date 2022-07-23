# Desenvolva um programa que pergunte a distância de uma viagem
# em Km. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = float(input('Qual a distância de viagem? '))
if dist <= 200:
    print ('O preço da passagem será de R${:.2f}'.format(dist*0.50))
else:
    print ('O preço da passagem será de R${:.2f}'.format(dist*0.45))