# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
# Dados de entrada = Kms percorridos, dias alugados, preço a pagar (dias *60, km*0,15)
km = int(input('Kms percorridos: Kms '))
dias = int(input('Dias de locação: '))
preço1 = dias*60
preço2 = km*0.15
preçot = preço1+preço2

print ('O valor referente às diárias foi de R${:.2f}\nO valor referente aos kms foi de R${:.2f}\nO valor total da locação foi de R${:.2f}.'.format(preço1, preço2, preçot))
