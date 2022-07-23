'''def soma(a, b):
    s = (a +b)
    print(f'A = {a}, B = {b}. A soma de A + B é {s}')
    print(s)

soma(4,5)'''

def area(larg, comp):
    a = (larg * comp)
    print(f'A área de um terreno de {larg}x{comp} é de {a}m²')


print('Área de um terreno')
print('-' *20)
larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
area(larg, comp)

'''soma(4, 3, 2)

def saudacao(msg= 'Oi', nome = 'João'):
    print (msg , nome)
saudacao()

def porcentagem(a, b):
    c= a * (b/100)
    res = a + c
    print(a+c)

porcentagem(50,10)

def fizzbuzz(n):
    for n in (3, 5):
        if n % 3 == 0 and n % 5 ==0:
            return 'FizzBuzz'
        if n % 3 == 0:
            return 'Fizz'
        elif n % 5 == 0:
            return 'Buzz'
        else:
            print (n)
from random import randint
aleatorio = randint(0, 100)
for aleatorio in randint(0, 100):
    print(fizzbuzz())
'''




