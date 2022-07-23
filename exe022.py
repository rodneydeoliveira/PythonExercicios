nome = str(input ('Digite seu nome: ')).strip()
print ('Seu nome em letras maiúsculas é', nome.upper())
print ('Seu nome em letras minúsculas é', nome.lower())
print ('Seu nome em tem ao todo {} letras' .format((len(nome) - nome.count(' '))))
#print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print ('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

