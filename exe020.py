from random import choice
nome = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro Aluno: '))
nome4 = str(input('último aluno: '))
lista = [nome, nome2, nome3, nome4]
sorteado = choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))