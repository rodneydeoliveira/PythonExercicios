'''
Operador ternário
'''
''' usuario_logado =  True
if usuario_logado == True: # ou if usuario_loagado:
    msg = 'Usuário logado'
else:
    msg = 'Você precisa logar'
print(msg)'''

usuario_logado = True
msg = 'Usuário logado' if (usuario_logado) else 'Você precisa logar'
print(msg)