alt = float(input('Qual a altura da parede?: '))
larg = float(input('Qual a largura da parede?: '))
area = alt * larg
tinta = area / 2**2
print('A área da parede é {}'.format(area))
print('Será necessário {} litros de tinta para pinta-la'.format(tinta))