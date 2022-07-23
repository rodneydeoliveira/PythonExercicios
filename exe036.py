'''

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em
 quantos anos ele vai pagar. A prestação
 mensal não pode exceder 30% do salário ou então o empréstimo será negado.
 Dados de entrada:
 Valor da casa =
  salário do comprador =
  quantos anos vai pagar =
  prestação <= a 30%
'''
casa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o seu salário atual? R$ '))
anos = int(input('Em quantos anos pretende pagar o imóvel? '))
prestacao = casa/anos/12
if prestacao <= (salario*30) / 100:
    print(f'Para comprar uma casa no valor de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}. Seu empréstimo foi APROVADO!')
else:
    print(f'Para comprar uma casa no valor de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}. Seu empréstimo foi NEGADO!')


