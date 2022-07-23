# Escreva um programa que converta uma temperatura digitando de Cº e converta para Fº
c = float(input('Digite a temperatura: Cº'))
f = (c* 9/5) + 32
k = c + 273.15
print ('A temperatura de {}º em Fahrenheit é de {}F.\nA temperatura de {}º em Kelvin é de {}K.'.format(c,f,c,k))
