t = n = 0
while True:
    if n <0:
        break
    n = int(input('Digite um numero para tabuada: '))
    for c in range (1,11):
        print(f'{n} X {c} = {n*c}')
        



