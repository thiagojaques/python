from math import sin, cos, radians, tan
angulo = float(input('Digite o ângulo para saber o valor do SENO, COSSENO e Tangente: '))
seno = sin(radians(angulo))
print('O valor do SENO é {:.2f}'.format(seno))
cosseno = cos(radians(angulo))
print('O valor do COSSENO é {:.2f}'.format(cosseno))
tangente = tan(radians(angulo))
print('O valor da TANGENTE é {:.2f}'.format(tangente))
