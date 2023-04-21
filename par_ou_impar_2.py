'''Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou ímpar. Caso o usuario não digite um número
inteiro, informe que não é um número inteiro.'''

numero = input('Digite um numero inteiro: ')


if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print('O número digitado é "PAR"')
    else:
        print('O número digitado é "IMPAR"')

else:
    print('O valor digitado nao é um numero inteiro')