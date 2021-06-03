print('==== Desafio 029 ====')
from random import randint
from time import sleep
pc = randint(0, 5)#faz o PC "PENSAR" randomizar
print('\033[33m-=-\033[m' * 20)
print('\033[36mVou pensar em um número entre 0 e 5. Tente Adivinhar...\033[m')
print('\033[33m-=-\033[m' * 20)

n = int(input('Em que número eu pensei?')) # Jogador tenta adivinhar
print('\033[1;34mPROCESSANDO...\033[m')
sleep(3)
if n == pc:
    print('\033[1;97;42m Parabens! Você Venceu \033[m')
else:
    print('\033[1;97;41m Errroooouu \033[m')
    print('Pensei no número {} e não no {}!'.format(pc,n))

