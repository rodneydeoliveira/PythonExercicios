'''
gerar um range de 19, onde, quando chegar no 9, devo subtrair esse numero por 9
exemplo: if n > 8 / n -= 9
7
8
9 - 9
10 - 9
11 - 9....
fórmula d = 11 - (total % 11)
if d > 9
    d = 0
'''


'''cpf = '42177911869'
novo_cpf = cpf[:-2]
reverso = 10
total = 0
for n in range(19):
    if n > 8:
        n -= 9

    total += int(novo_cpf[n]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)'''


cpf = str(input('Digite seu CPF: ')).replace('.','').replace('-','')

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
print(d1)

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
print(d2)

if d1 == int(cpf[9]) and d2 == int(cpf[10]):
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')