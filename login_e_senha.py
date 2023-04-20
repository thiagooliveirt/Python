entrada = input('[E]ntrar [S]air: ')

if entrada == 'S' or entrada == 's':
    print('Saindo...')
else:
    senha_digitada = input('Senha: ')
    senha_permitida = '123456'

    if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
        print('Login Efetuado!')
    else:
        print('Senha Incorreta')

