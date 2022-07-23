s = c = 0
while True:
    n = int(input('Digite um valor ou 999 para parar: '))
    if n == 999:
        break
    c += 1
    s = s + n

print (f'Você digitou {c} valores e a soma deles foi {s}')