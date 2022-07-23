#Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
sal = float(input('Digite o seu salário: '))
if sal <= 1250:
    aumento = (sal*15) //100
else:
    aumento = (sal*10) // 100
print ('Com o reajuste o seu salário atual é de R%{:.2f}'.format(sal+aumento))