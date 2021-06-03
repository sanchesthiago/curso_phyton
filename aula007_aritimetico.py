n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2

print('A soma é {},  A multiplicação é {}, A divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} Potencia {}'.format(di, p))
