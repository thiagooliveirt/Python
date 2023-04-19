#Verifique se uma pessoa é maior ou menor de idade.

idade = input('Digite sua idade: ')
id = int(idade)

if id >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')