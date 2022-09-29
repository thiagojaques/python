from math import hypot

'''Soma dos catetos com importação de biblioteca'''

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hip))


''' Soma dos catetos do modo matemático padrão'''

cos = float(input('Digite o valor do cateto oposto: '))
cat = float(input('Digite o valor do cateto adjacente: '))
hipo = (co **2 + ca **2) ** (1/2)
print('O valor da hipotenusa vai ser {:.2f}'.format(hipo))
