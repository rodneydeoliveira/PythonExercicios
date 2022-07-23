'''dados = {}
dados ['nome'] = 'Pedro'
dados ['idade'] = '25' # Adiciona índices e valores à chave
dados ['sexo'] = 'M'
del dados['idade'] # Deleta o índice (chave) e o seu valor
print(dados)

#         Chave      Valor      Chave  Valor   Chave        Valor
filme = {'Título': 'Star Wars', 'Ano': '1977', 'Diretor': 'George Lucas'}

# Para acessar somente as chaves devemos usar o método .keys() / Ex print(filme.keys())
# Para acessar os valores usamos o método .values() /Ex print(filme.values())
# Para acessar chaves e valores, usamos o método .items() / print(filme.items())

for chave, valor in filme.items():
    print (f'O {chave} é {valor}')

brasil = list()
estado1 = {'UF': 'Rio de Janeiro' ,'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]) # O valor exibido será o estado1
print(brasil[1]['sigla']) # O valor exibido será SP

# ADICIONANDO ITENS NA LISTA ATRAVÉS DO INPUT

est = dict()
brasil2 = list()

for contador in range (0,3): #Iremos adicionar 3 estados na lista
    #    K                    V
    est ['UF'] = input('Nome do Estado: ') # Input nome do estado
    est ['sigla'] = input('Sigla do estado:') # Input sigla do estado
    brasil2.append(est.copy()) # Adicionando os valores a lista, e salvando
    # as informações com o método 'copy', antes de iniciarmos um novo laço
# A variavel 'brasil2' terá 3 estados e 3 silgas

for estado in brasil2: # irá exibir os 3 estados e suas silgas dentro das chaves
    for k, v in estado.items(): # Para cada chave e valor dentro dos itens de estado:
        print(f'{k} = {v}')'''


estado = dict()
brasil = list()

for contador in range (0,3):
    #       k                   v
    estado['UF'] = input('Nome do estado: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())

for valor in brasil:
    for chave, v in valor.items():
         print(f'O valor {chave} é {v}')