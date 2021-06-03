import random

print('======Desafio020=====')
alu1 = str(input('Primeiro Aluno: '))
alu2 = str(input('Segundo Aluno: '))
alu3 = str(input('Terceiro Aluno: '))
alu4 = str(input('Quarto Aluno: '))

lista = [alu1, alu2, alu3, alu4]
escolhido = random.choice(lista)

print('O nome escolhido pelo Professor é: {}'.format(escolhido))
