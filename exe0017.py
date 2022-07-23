'''from math import hypot
num1 = float(input('Comprimento do cateto oposto: '))
num2 = float(input('comprimento do cateto adjacente: '))
hip = hypot(num1, num2)
print ('a hipotenusa vai medir {:.2f}'.format(hip))'''

num1 = float(input('Comprimento do cateto oposto: '))
num2 = float(input('Comprimento do cateto adjacente: '))
hip = (num1**2 + num2**2) **(1/2)
print ('A hipotenusa vai medir {:.2f}'.format(hip))



