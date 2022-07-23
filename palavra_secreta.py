secreto = 'perfume'
digitadas = []
chances = 3
while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ahh, isso não vale. Digite apenas uma letra')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'Muito bem, a letra {letra} contém na palavra secreta ')
    else:
        print(f'Ahh, a letra {letra} não contém na palavra secreta')
        digitadas.pop()
        chances -= 1
        print(f'Você tem {chances} chances')
        if chances <= 0:
            print('Suas chances acabaram, você perdeu')
            break

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
        else:
             secreto_temporario += '*'
    print(secreto_temporario)
    if secreto_temporario == secreto:
        print(f'Parabéns, você ganhou. A palavra secreta era {secreto}')
        break

