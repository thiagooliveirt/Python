entrada = input('[E]ntrar [S]air: ')

if entrada == 'S':
    print('Saindo...')
else:
    senha_digitada = input('Senha: ')
    senha_permitida = '123456'

    if entrada == 'E' and senha_digitada == senha_permitida:
        print('Login Efetuado!')
    else:
        print('Senha Incorreta')
