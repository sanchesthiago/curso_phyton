print('=====Desafio029=====')
vel=int(input('Velocidade Atual do Veiculo: '))
if vel<=80:
    print('\033[4;32mTenha um bom dia!\033[m \n\033[1;36mDirija com Segurança\033[m')
else:
    print('\033[1;97;41mMULTADO!\033[m \033[31mVocê Excedeu o limite permitido de 80km/h\033[m')
    print('Sua Multa é de: \033[4;97mR${}\033[m'.format((vel-80)*7))
    print('Voce excedeu {}km/h do permitido'.format(vel-80))
