print('==== Desafio0026====')
frase = str(input('Digite uma Frase:')).strip().lower()

print('A letra A aparece {} na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A Ultima letra A apareceu na posição {}'.format(frase.rfind('a')+1))

