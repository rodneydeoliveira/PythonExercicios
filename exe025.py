# Crie um programa que leia o nome de uma pessoa
# diga se ela tem “SILVA” no nome.
nome = str(input('Digite seu nome completo: ')).strip()
sil = ('silva' in nome.lower())
print('Seu nome tem Silva?',sil)