#Verifique se um número é positivo, negativo ou zero.

numero_1 = input('Digite um numero: ')
n1 = int(numero_1)

if n1 < 0:
    print('Negativo')
elif n1 == 0:
    print('Numero Zero')
else:
    print('Positivo')

