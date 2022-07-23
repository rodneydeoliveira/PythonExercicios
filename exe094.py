pessoa = dict()
galera = list()
contador_idade = média = 0
mulheres = 0
while True:
    pessoa.clear()
    pessoa ['nome'] = str(input('Nome: '))
    while True:
        pessoa ['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa ['sexo'] == 'F':
            mulheres +=1
        if pessoa ['sexo'] in 'MF':
            break

        print('ERROR 404. Digite apenas M/F')
    pessoa ['idade'] = int(input('Idade: '))
    contador_idade += pessoa ['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERROR 404. Digite apenas S ou N ')
    if resposta == 'N':
         break
print('-=' *20)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = contador_idade / len(galera)
print(f'A média de idade é de {média:.2f} anos')
print(f'Foram cadastradas um total de {mulheres} mulheres')

print(f'Lista das pessoas que estão acima da média, ')
for p in galera:
    if p['idade'] >= média:
        print("   ")
        for k, v in p.items():
            print(f'{k} = {v}', end='')
print('<< ENCERRADO >>')