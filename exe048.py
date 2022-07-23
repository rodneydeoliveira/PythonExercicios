soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont += 1
print (f'A soma de {cont} todos os valores é {soma}')