n: str = input('Digite algo:')
print('o tipo primitivo é{}'.format(type(n)))
print('Alfa Numerico: {}'.format(n.isalnum()))
print('O Texto esta em caixa Baixa: {}'.format(n.islower()))
print('O Texto esta em caixa Alta: {}'.format(n.isupper()))
print('O Texto são Números: {}'.format(n.isdecimal()))
print('O Texto tem apenas sequencia de espaco: {}'.format(n.isspace()))
print('O Texto está capitalizado?: {}'.format(n.istitle()))


