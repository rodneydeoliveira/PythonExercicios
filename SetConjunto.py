# Set ou conjunto, são representados pelo símbolo de chaves {}
# Porém, diferente dos dicionários, set não recebe par de 'valores' (chave:valor)
# Set recebe apenas valores individuais {1, 2, 'Rodney', (345),} etc...
# Set não permite elemento duplicados. Podemos converter listas em set se quisermos
# Eliminar os elementos duplicados. Basta fazer um CAST para lista
set1 = {1, 2, 3, 'Rodney'}
set1.add (1)
set1.add ('Corinthians')
set1.discard('Rodney')
print(set1)

lista = [1,2,3,4,5,5,5,5,'rod', 'rod']
set2 = set(lista) # variavel lista agora é set. Elementos duplicados foram eliminados
set2 = list(set2) # A variavel set2 voltou a ser uma lista, sem os elementos duplicados
print(set2)

a1 = 2