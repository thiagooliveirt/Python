nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print('{} esta em {}'.format(encontrar, nome))
else:
    print('{} não esta em {}'.format(encontrar, nome))