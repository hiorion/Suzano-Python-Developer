def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido! Só é possível depositar valores positivos.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("Valor inválido! Digite um valor positivo.")
    elif valor > saldo:
        print("Saldo insuficiente para o saque.")
    elif valor > limite:
        print(f"O valor do saque excede o limite de R$ {limite:.2f} por operação.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques diários atingido.")
    else:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO =====")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("===================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    # Verifica se CPF já existe
    if any(u['cpf'] == cpf for u in usuarios):
        print("Usuário com esse CPF já cadastrado!")
        return

    nome = input("Informe o nome completo: ").strip()
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ").strip()

    usuario = {
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário para vincular a conta: ").strip()
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario is None:
        print("Usuário não encontrado! Conta não criada.")
        return None

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    print(f"Conta criada com sucesso! Agência: {agencia}, Número: {numero_conta}, Titular: {usuario['nome']}")
    return conta


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    print("\n=== Lista de Contas ===")
    for conta in contas:
        u = conta["usuario"]
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {u['nome']} | CPF: {u['cpf']}")
    print("========================")


def main():
    saldo = 0.0
    limite_saque = 500.0
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        print("""
===== MENU =====
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[6] Listar Contas
[0] Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite_saque,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Encerrando o sistema. Obrigado!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
