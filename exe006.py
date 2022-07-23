# Faça um programa que receba um valor e exiba o seu dobro, triplo e raíz quadrada.

n = int(input('Digite um valor: '))
d = n*2
t = n*3
r = n**(1/2)
print ('O dobro desse valor é {}\nO triplo é {}\nA raiz quadrada é {:.3f} '.format(d, t, r))

