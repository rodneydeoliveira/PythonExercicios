# Ler o nome, ano de nasc, numero da ctps, ano de contratação e guardar no dict
from datetime import datetime


funcionario = {}
funcionario ['Nome '] = str(input('Digite seu nome: '))
nasc = int(input('Ano de nascimento: '))
funcionario ['Idade'] = datetime.now().year - nasc
funcionario ['CTPS'] = int(input('CTPS: '))
if funcionario['CTPS'] != 0: # se o numero da CTPS for 0, não teremos mais informações recebidas pelo input
    funcionario ['Salário'] = float(input('Salário: R$'))
    funcionario['Ano de contratação'] = int(input('Ano de contratação: '))

print('-=' *20)
for chave, valor in funcionario.items():
    print(f'   - {chave} tem valor {valor}')
print('-=' *20)