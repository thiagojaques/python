from random import shuffle
n1 = str(input('Primeiro nome da lista: '))
n2 = str(input('Segundo nome da lista: '))
n3 = str(input('Terceiro nome da lista: '))
n4 = str(input('Quarto nome da lista: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem será')
print(lista)