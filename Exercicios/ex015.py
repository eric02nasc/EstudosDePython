d = float(input('Quantos dias foi usado o carro? '))
k = float(input('Quantos Km foram rodados? '))
v = (k*0.15) + (d*60)
print('O valor do aluguel é de R${:.2f}'.format(v))