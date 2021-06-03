print('====Desafio030====')
n=int(input('\033[34mDigite um Número: \033[m'))
if n % 2 == 0:
    print('O numero {} é \033[1;35mPAR\033[m'.format(n))
else:
    print('O Numero {} é \033[1;36mÍMPAR\033[m'.format(n))
