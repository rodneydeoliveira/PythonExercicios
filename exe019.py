import math
a = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, tan))

