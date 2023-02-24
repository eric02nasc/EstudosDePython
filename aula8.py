# from math import sqrt, floor
# n = int(input('Digite um número: '))
# r = sqrt(n)
# print('O valor da raiz quadrada de {} é {}'.format(n, floor(r)))

# import random
# num = random.randint(0,5)
# print(num)


from random import randint
p1 = int(input('Escolha um número\nLembrando que 1 é pedra, 2 é papel, 3 tesoura: '))

p2 = randint(1, 3)
print('O número escolhido pelo seu adversário foi {}'.format(p2))

# empate
if (p1 == 1 and p2 == 1 or p1 == 2 and p2 == 2 or p1 == 3 and p2 == 3):
    print('Empatou')
# vitoria
elif (p1 == 1 and p2 == 3 or p1 == 2 and p2 == 1 or p1 == 3 and p2 == 2):
    print('Você venceu')
# derrota
elif (p1 == 1 and p2 == 2 or p1 == 2 and p2 == 3 or p1 == 3 and p2 == 1):
    print('Seu adversário venceu')



