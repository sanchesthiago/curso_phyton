print('====Desafio031=====')
dist = float(input('Qual a distancia da sua viagem?'))
print('Você esta prestes a começar uma viagem de {} km'.format(dist))
if dist <= 200:
    print('o preço da sua passagem será de: R${:.2f}'.format(dist*0.50))
else:
    print('Preço da sua passagem sera de: R${:.2f}'.format(dist*0.45))