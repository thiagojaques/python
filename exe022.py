from itertools import count


frase = str(input('Digite o seu nome completo?: ')).strip()
print('Analisando seu nome...')
print('Assim fica com todas as letra maiúsculas: {}'.format(frase.upper()))
print('Com todas minúsculas: {}'.format(frase.lower()))
print('{} tem {} letras.'.format(frase, len(frase)- frase.count(' ')))
separa = frase.split()
print('Seu primeiro nome é {}, e tem {} letras.'.format(separa[0], len(separa[0])))