
'''Chaves podem armazenar qualquer valor imutável
Ex.: Strings, int e tuplas
     |chave|   |      valor     |
d1 = {'str': 'Valor da chave str',
      1234: 'Valor da chave int',
      (1, 2, 3, 4, 5): 'Valor da chave em tupla
}'''

# del d1['str'] Apaga a chave e o seu valor
# print('str' in d1)# Verifica se a chave existe na variavel
# print('str' in d1.keys())         # ||
# print('Valor da chave int' in d1.values()) # Verifica se o valor existe na variavel

# print(len(d1)) # Veridica quantos pares de chave contém na variável
'''d2 = {'chave1': 'valor da chave1',
      'chave2': 'valor da chave2',
      'chave3': 'valor da chave3'
      }
for k in d2: # Acessa somente as chaves
    print(k)

for v in d2.values(): # Acessa somente os valores
    print(v)

for k, v in d2.items(): # Acessa as chaves e os valores
    print(k, v)'''

'''familia = {
    'filho 1': {
        'nome' : 'Kaio',
        'idade': 33,
    },

    'filho 2': {
        'nome': 'Renan',
        'idade': 30
         },
    'filho 3': {
        'nome': 'Rod',
        'idade': 28
         }

    }


for f, n in familia.items():
    print(f'Exibindo {f}')
    
    for dados_k, dados_v in n.items():
        print(f'\t{dados_k} = {dados_v}')'''


perguntas = {
    'Pergunta 1':{
        # PK             #PV
        'pergunta': 'quanto é 2+2? ',# CHAVE PERGUNTA - VALOR 'QUANTO É...'
        'alternativas' : {'a':'1', 'b': '2', 'c': '4'}, # CHAVE 'ALTERNATIVAS'
        'resposta certa': 'c'
    } ,
'Pergunta 2':{
        'pergunta': 'quanto é 3+4? ',
        'alternativas' : {'a':'5', 'b': '7', 'c': '9'},
        'resposta certa': 'b'
}
}

for pk, pv in perguntas.items():
    print(f'{pk} : {pv["pergunta"]}')
    for dados_k, dados_v in pv['alternativas'].items():
        print(f'[{dados_k}]= {dados_v}')

    resposta_usuario = input('Digite a sua resposta: ')
    if resposta_usuario == pv['resposta certa']:
        print('você acertou')
    else:
        print('Você errou')
        