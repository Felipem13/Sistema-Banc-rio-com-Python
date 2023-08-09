
def sacar(*,saldo,valor,extrato,limite,n_saques,limite_saque):

    if n_saques > limite_saque:
        print('Limite de Saque Atingido')
    elif valor > saldo:
        print(f'Saldo insuficiente para Saque!')
    elif valor > limite:
        print('Valor de saque excede o limite!')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}\n'
        n_saques += 1
    return saldo,extrato

def deposito(saldo,valor,extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}\n'
        return saldo,extrato
    else:
        return print('Valor informado é inválido')

def extrato_banco(saldo,/,*,extrato):
    print(f'=========== EXTRATO BANCÁRIO ==========')
    #print('Não foi realizado movimentações em conta' if not extrato else extrato)
    if not extrato:
        print('Não foram realizados movimentações')
    else:
        print(extrato)
        print(f'Saldo Atual: R${saldo:.2f}')
        print('=======================================')
    return

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente númerios): ')

    if cpf.isnumeric() and len(cpf) == 11:
        if filtrar_usuario(cpf,usuarios):
            print("CPF Já Existe")
            return
        else:
            nome = input("Informe nome completo: " ).upper()
            data_nascimento = input("Informe a data de nascimento (dd/mm/yyyy): ")
            endereço = input("Informe o endereço (Logradouro, nro - bairro - cidade/sigla estado): ")
            usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereço":endereço})
            print("-"*5,"Usuário criado com sucesso","-"*5)
    else:
        print("CPF inválido")
        return
def filtrar_usuario(cpf,usuarios):
        usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(numero_conta,usuarios,AGENCIA="0001"):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia":AGENCIA,"numero_conta":numero_conta,"usuario":cpf}

    print("-----Usuário não encontrado, fluxo de criação de conta encerrado")

def lista_costas(contas):
    for conta in contas:
        linha =f'''
        Agência:\t{conta['agencia']}
        C/C:\t{conta['numero_conta']}
        Titular:\t{conta['usuario']}
        '''
        print('-'*100)
        print(linha)

def main():
    clientes = []
    contas = []
    saldo = 0
    extrato = ''
    n_saques = 0
    SAQUE_LIMITE = 3
    LIMITE = 500

    MENU = '''
    [d]   Depositar
    [s]   Sacar
    [e]   Extrato
    [nc]  Nova Conta
    [lc]  Listar Contas
    [nu]  Novo Usuário
    [q]   Sair
    =>'''

    while True:

        opcao = input(MENU).lower().strip()

        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))
            saldo,extrato = deposito(saldo,valor,extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor à sacar: '))
            saldo, extrato = sacar(
                                    saldo=saldo,
                                    valor=valor,
                                    extrato=extrato,
                                    limite=LIMITE,
                                    n_saques=n_saques,
                                    limite_saque=SAQUE_LIMITE)

        elif opcao == 'e':
            extrato_banco(saldo,extrato)
        elif opcao == 'q':
            break
        elif opcao == 'nu':
            criar_usuario(clientes)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(numero_conta,clientes)
            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            lista_costas(contas)
        else:
            print('Comando Inválido')
main()