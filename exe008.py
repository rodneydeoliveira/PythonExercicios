# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
m = float(input('Digite um valor: '))
cm = m*100
mm = m*1000
dm = m*10
dam = m/10
hm = m/100
km = m/1000
print ('A medida de {} m corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mi'.format(m, km, hm, dam,dm,cm, mm ))
