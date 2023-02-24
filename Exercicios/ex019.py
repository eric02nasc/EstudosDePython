from random import choice
a = str(input('Qual o nome do primeiro aluno?'))
b = str(input('Qual o nome do segundo?'))
c = str(input('Qual o nome do terceiro?'))
d = str(input('Qual o nome do último?'))

lista = [a, b, c, d]

print('O aluno escolhido é {}'.format(choice(lista)))
