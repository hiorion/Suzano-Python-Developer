# ===========================================
# OBJETIVO GERAL:
# Criar um sistema bancário com as operações:
# - Depositar
# - Sacar
# - Visualizar extrato
# ===========================================

# Variáveis principais
saldo = 0.0
limite_saque = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Menu principal
while True:
    print("\n===== MENU =====")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    # Operação DEPÓSITO
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido! Só é possível depositar valores positivos.")

    # Operação SAQUE
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente para o saque.")
        elif excedeu_limite:
            print(f"O valor do saque excede o limite de R$ {limite_saque:.2f} por operação.")
        elif excedeu_saques:
            print("Número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido! Digite um valor positivo.")

    # Operação EXTRATO
    elif opcao == "3":
        print("\n===== EXTRATO =====")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===================")

    # Sair
    elif opcao == "0":
        print("Encerrando o sistema. Obrigado!")
        break

    # Opção inválida
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
