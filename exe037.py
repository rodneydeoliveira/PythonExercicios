# Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número qualquer: '))
print ('Escolha sua opção: ')
print ('[1] Binário \n[2] Octal \n[3] Hexadecimal ')
opc = int(input('Qual base de conversão você deseja escolher?: '))
if opc == 1:
    print (f'O número {num} convertido para Binário é {bin(num)[2:]}')
elif opc == 2:
    print (f'O número {num} convertido para Octal é {oct(num)[2:]}')
elif opc == 3:
    print (f'O número {num} convertido para Hexadecimal é {hex(num)[2:]}')
else:
    print ('Opção Inválida. Tente novamente!')

