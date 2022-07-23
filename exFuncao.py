'''
Crie uma funcao1 que receba uma funcao2 como parâmetro e retorne o valor
da funcao2 executada
'''
def ola_mundo():
    return 'Olá Mundo!!!'

def func2(funcao):
    return funcao()

executando = func2(ola_mundo)
print(executando)