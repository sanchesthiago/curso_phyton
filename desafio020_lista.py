import random

print('=======Desafio020======')
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('A ordem de apresentação sera: \n{}'.format(lista))
