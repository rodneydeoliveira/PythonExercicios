"""Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade, se ele ainda vai se alistar ao
serviço militar, se é a hora exata de se alistar ou
se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo"""
import datetime

nasc = int(input('Ano de Nascimento: '))
from datetime import date
ano = date.today().year
idade = (ano - nasc)
if idade < 18:
    saldo = 18 - idade
    print (f'Sua idade é de {idade} anos. Você deve se alistar daqui {saldo} ano(s)')
elif idade > 18:
    saldo = idade - 18
    print(f'Sua idade é de {idade} anos. Você deveria ter se alistado em {saldo} ano(s)')
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')