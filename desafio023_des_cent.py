print('======Desafio023=====')

numero = int (input('informe um numero:'))
uni = numero //1 % 10
dez = numero //10 % 10
cen = numero //100 % 10
mil = numero // 1000 % 10
print('Analizando o numero {}...'.format(numero))

print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena {}'.format(cen))
print('Centena {}'.format(mil))