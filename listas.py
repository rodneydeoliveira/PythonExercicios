
# Listas podem armazenar mais de um valor, e diferentes tipos de dados
# índice 0  1  2  3  4
lista = [1, 2, 3, 4, 5]
# -      5  4  3  2  1

l1 = [1, 2, 3]
l2 = [4, 5, 6]
# o sinal de + concatena as duas listas (juntam)
print('Concatena')
l3 = l1 + l2
l1.extend(l2)
# Extend faz uma extensão da lista com a outra, sendo que a segunda lista continua
# existindo separadamente
print(l1)
print(l2)
print(l3)
# Append insere valores  no FINAL da lista
l2.append('B')
print('Append')
print(l2)
# Insert adiciona valores no ÍNDICE que escolhemos
l2.insert(0, 'Banana')
print ('Insert')
print (l2)
# Pop exclui o último valor da lista
l2.pop()
print('Pop')
print(l2)
# Del delete o(s) índice(s) que eu escolher
del (l2[1])
print('Del')
print(l2)
# Min e Max exibem os valores Mínimo e Máximo da lista (suporta apenas números)
print('Min e Max - apenas números')
print (min(lista))
print(max(lista))

lista2 = list (range(0,20))
print(lista2)