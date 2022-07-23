# aça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
# altura  largura   area m²  Litros = area/2
altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura*largura
litros = area/2
print ('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede, você precisará de {}l de tinta.'.format(altura,largura,area,litros
                                                                                                                                  ))