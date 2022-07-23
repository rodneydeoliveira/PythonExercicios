from random import randint
def mensagem_formatada():
	print("************************************************************")


def jogar():
	valor_aleatorio = randint (1, 100)
	tentativas = 5

	while tentativas >=1:
		chute = int(input("chute um numero de 1 a 100: "))
		if chute == valor_aleatorio:
			print("Você acertou")
		elif chute > valor_aleatorio:
			tentativas -=1
			mensagem_formatada()
			print("Chute maior que valor gerado. Você tem {} tentativa(s). ".format(tentativas))
			mensagem_formatada()
		elif chute < valor_aleatorio:
			tentativas -=1
			mensagem_formatada()
			print("Chute menor que valor gerado. Você tem {} tentativa(s). ".format(tentativas))
			mensagem_formatada()
		else:
			print("Digite um número entre 1 e 100 apenas. Você tem mais {} tentativa(s)".format(tentativas))

	print ("Fim de jogo")
	print(f'O valor gerado foi {valor_aleatorio}')

if __name__ == "__main__":
	jogar()