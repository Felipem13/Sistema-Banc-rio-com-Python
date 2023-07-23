MENU = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>'''

saldo = 0
extrato = ''
n_saques = 0
SAQUE_LIMITE = 3
LIMITE = 500

while True:

    opcao = input(MENU).lower().strip()

    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'
        else:
            print('Valor informado é inválido')

    elif opcao == 's':
        valor = float(input('Informe o valor à sacar: '))

        if n_saques >= SAQUE_LIMITE:
            print('Limite de Saque Atingido')

        elif valor > saldo:
            print(f'Saldo insuficiente para Saque!')

        elif valor > limite:
            print('Valor de saque excede o limite!')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n'
            n_saques += 1

        else:
            print('Operação Falhou! Valor Inválido')

    elif opcao == 'e':
        print(f'=========== EXTRATO BANCÁRIO ==========')
        #print('Não foi realizado movimentações em conta' if not extrato else extrato)
        if not extrato:
            print('Não foram realizados movimentações')
        else:
            print(extrato)
        print(f'Saldo Atual: R${saldo:.2f}')
        print('=======================================')

    elif opcao == 'q':
        break

    else:
        print('Comando Inválido')
