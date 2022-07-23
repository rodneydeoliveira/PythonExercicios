# Faça um programa que receba o valor do produto e exiba o preço com 5% de desconto

preço = float(input('Digite o valor do produto: R$'))
desconto = (preço*5/100)
print ('O valor do produto com desconto é de R${:.2f}.'.format(preço-desconto))
