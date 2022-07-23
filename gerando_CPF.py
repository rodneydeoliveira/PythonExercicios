from random import randint

cpf = str(randint(100000000, 999999999))

resultado = 0
acumulador = 0
contador = 10
for n in cpf[0:9]:
    resultado = int(n) * contador
    acumulador += resultado
    contador -= 1
d1 = 11 - (acumulador % 11)

if d1 >9:
    d1 = 0
cpf += str(d1)

resultado2 = 0
acumulador2 = 0
contador2 = 11

for n in cpf[0:10]:
    resultado2 = int(n) * contador2
    acumulador2 += resultado2
    contador2 -= 1
d2 =  11 - (acumulador2 % 11)
if d2 >9:
    d2 = 0
cpf += str(d2)
print(cpf)
