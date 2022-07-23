# Exercício: Pegar o nome do aluno, média da nota e dizer a situação

aluno = dict()
aluno ['nome'] = input('Nome do aluno: ')
aluno ['média'] = float(input(f'Média do {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5:
     aluno['situação'] = 'Recuperação'
else:
     aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')


