# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
sal = float(input('Digite o seu salário: R$'))
aumento = (sal*15/100)
print ('O seu salário com reajuste será de R${:.2f}'.format(sal+aumento))