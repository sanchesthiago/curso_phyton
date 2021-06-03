import math

print('=====Desafio018=====')
angu = float(input('Digite o Angulo: '))

se = math.sin(math.radians(angu))
cos = math.cos(math.radians(angu))
tang = math.tan(math.radians(angu))

print('Para o Angulo {:.2f} temos:\n Seno={:.2f}\n Cosseno={:.2f}\n Tangente={:.2f}'.format(angu, se, cos, tang))