# Sistema Bancário em Python - Versão 1

## Desafio

Fomos contratados por um grande banco para desenvolver a primeira versão de seu novo sistema bancário. A proposta é permitir operações básicas de um único usuário: depósitos, saques e visualização de extrato.

---

## Requisitos

### Operação de Depósito
- Deve aceitar apenas valores positivos.
- O valor deve ser somado ao saldo.
- A operação deve ser registrada para exibição no extrato.

### Operação de Saque
- Permitir no máximo 3 saques por dia.
- Cada saque pode ter valor máximo de R$ 500,00.
- O saque deve ser recusado se o saldo for insuficiente.
- Cada saque também deve ser registrado no extrato.

### Operação de Extrato
- Listar todos os depósitos e saques.
- Exibir o saldo atual da conta.
- Os valores devem ser formatados no padrão R$ xxx.xx.

---

## Código-Fonte com Comentários

```python
# Sistema Bancário - Operações: depósito, saque e extrato

# Inicialização das variáveis principais
saldo = 0.0  # Saldo da conta
limite_saque = 500.0  # Limite por saque
extrato = ""  # Histórico de movimentações
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Limite máximo de saques por dia

# Loop principal do menu
while True:
    print("\n===== MENU =====")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    # ============================
    # OPERAÇÃO DE DEPÓSITO
    # ============================
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor  # Atualiza o saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra no extrato
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido. Digite um valor positivo.")

    # ============================
    # OPERAÇÃO DE SAQUE
    # ============================
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente para o saque.")
        elif excedeu_limite:
            print(f"O valor excede o limite de R$ {limite_saque:.2f}.")
        elif excedeu_saques:
            print("Limite diário de saques atingido.")
        elif valor > 0:
            saldo -= valor  # Reduz o saldo
            extrato += f"Saque:    R$ {valor:.2f}\n"  # Registra no extrato
            numero_saques += 1  # Incrementa o número de saques
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido. Digite um valor positivo.")

    # ============================
    # OPERAÇÃO DE EXTRATO
    # ============================
    elif opcao == "3":
        print("\n===== EXTRATO =====")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===================")

    # ============================
    # ENCERRAR O SISTEMA
    # ============================
    elif opcao == "0":
        print("Encerrando o sistema. Obrigado por utilizar nossos serviços.")
        break

    # ============================
    # OPÇÃO INVÁLIDA
    # ============================
    else:
        print("Opção inválida. Tente novamente.")
````