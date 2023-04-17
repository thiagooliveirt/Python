nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = int(input('Digite sua idade: '))
ano_nascimento = input('Digite o seu ano de nascimento: ')
altura_metros = input('Digite sua altura: ')

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('Altura em metros:', altura_metros)
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')