print('======Desafio 022 ======')

nome: str = str(input('Digite seu nome completo:')).strip()

print('Nome em Maiusculo: {}'.format(nome.upper()))

print('Seu Nome em Miniusculo: {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

separa=nome.split()

print('Seu primeiro nome é: {} e ele tem {} Letras '.format(separa[0], len(separa[0])))