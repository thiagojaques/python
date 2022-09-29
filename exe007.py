n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um terceiro número: '))
soma = n1 + n2 + n3
mult = n1 * n2 * n3
sub = n1 - n2 - n2
divisao = n1 / n2 / n2
resto = n1 % n2
print('A soma dos números: {} + {} + {} = {}'.format(n1,n2,n3,soma), end=' >>>')
print('A multiplação dos números: {} * {} * {} = {}'.format(n1,n2,n3,mult))
print('A subtração dos números: {} - {} - {} = {}'.format(n1,n2,n3,sub))
print('A divisão dos números: {} / {} / {} = {}'.format(n1,n2,n3,divisao))
print('O resto da divisão dos números: {} % {} = {}'.format(n1,n2,resto))