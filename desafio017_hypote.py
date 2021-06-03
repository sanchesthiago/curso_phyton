import math

print('=====Desafio017=====')
co = float(input('Cateto oposto: '))
ca = float(input('Cateto Adjacente: '))
hp = math.hypot(co, ca)

print('Cateto Oposto = {}\nCateto Adjacente = {}\nHypotenuza = {}'.format(co,ca,hp))