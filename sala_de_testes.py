# cpf = str(input('Digite seu CPF: ')).replace('.','').replace('-','')
'''
Validando CPF
Gerando CPF
'''

cpf = str('59184103256')
novo_cpf = cpf[0:9]
contador = 10
resultado = 0
acumulador = 0


for n in novo_cpf[0:9]:
    resultado = int(n) * contador
    acumulador += resultado
    contador -= 1
d1 = 11 - (acumulador % 11)
if d1 >= 10:
    d1 = 0
novo_cpf += str(d1)

resultado2 = 0
acumulador2 = 0
contador2 = 11
for n in novo_cpf[0:10]:
    resultado2 = int(n) * contador2
    acumulador2 += resultado2
    contador2 -= 1


d2 = 11 - (acumulador2 % 11)
if d2 >=10:
    d2 = 0

novo_cpf += str(d2)

print(cpf)
print(novo_cpf)

if cpf == novo_cpf:
    print('CPF Válido')
else:
    print('CPF Inválido')