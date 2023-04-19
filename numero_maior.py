#Calcule o maior entre dois números.

numero_1 = input('Digite o primeiro numero: ')
numero_2 = input('Digite o segundo numero: ')

n1 = int(numero_1)
n2 = int(numero_2)

if n1 > n2:
    print('Primeiro numero é maior')
elif n2 > n1:
    print('Segundo numero é maior')
else:
    print('Numeros iguais')