print('====Desafio033====')
from datetime import date
ano=int(input('Qual Ano Você quer analizar? Coloque 0 para analizar o ano atual: '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 ==0:
    print('O Ano de {} é bissexto'.format(ano))
else:
    print('O Ano {} não é bissexto'.format(ano))