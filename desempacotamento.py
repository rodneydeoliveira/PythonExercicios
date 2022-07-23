'''

Desempacotamento em Python

'''
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9]
n1, n2, n3, *resto_da_lista, ultimo_da_lista = lista
print(resto_da_lista, ultimo_da_lista)
