menu = '''
       Seja bem vindo ao POORBANK
       
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
'''
print(menu)

saldo = 1000
extrato = saldo
numero_saques = 0
LIMITE_SAQUE = 3
LIMITE_VALOR_SAQUE = 500  # Adicione o limite de valor de saque

while numero_saques < LIMITE_SAQUE:
    opcao = int(input('Digite a opção: '))

    if opcao == 1:
        deposito = float(input('Digite o valor do depósito: '))
        saldo += deposito
        print('Depósito efetuado com sucesso!')
        extrato = saldo
    elif opcao == 2:
        saque = float(input('Digite o valor do saque: '))
        if saque <= saldo and saque <= LIMITE_VALOR_SAQUE:  # Verifique o limite de valor de saque
            saldo -= saque
            extrato = saldo
            numero_saques += 1
            print('Saque efetuado com sucesso!')
        elif saque > LIMITE_VALOR_SAQUE:
            print(f'Limite de valor de saque excedido. O limite é de R${LIMITE_VALOR_SAQUE:.2f}')
        else:
            print('Saque indisponível')
    elif opcao == 3:
        print(f'Saldo: R${extrato:.2f}')
    elif opcao == 4:
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')

    if numero_saques >= LIMITE_SAQUE:
        print('Limite de saques atingido. Não é possível realizar mais saques.')

print('Obrigado por usar o POORBANK!')
