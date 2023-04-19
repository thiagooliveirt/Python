#Verifique se um ano é bissexto ou não.

ano = input('Digite um ano: ')
year = int(ano)

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('Ano Bissexto')
else:
    print('O ano NÃO é Bissexto')