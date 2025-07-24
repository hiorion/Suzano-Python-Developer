class ContaBancaria:
    banco = "Banco Orion"
    total_contas = 0

    def __init__(self, titular, saldo_inicial, senha):
        self.titular = titular
        self._saldo = saldo_inicial
        self.__senha = senha
        ContaBancaria.total_contas += 1

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("Erro: saldo negativo.")

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova):
        if len(nova) >= 4:
            self.__senha = nova
            print("Senha alterada com sucesso.")
        else:
            print("Senha muito curta.")

    def mostrar_dados(self):
        print(f"\nTitular: {self.titular}")
        print(f"Banco: {ContaBancaria.banco}")
        print(f"Saldo: R${self._saldo:.2f}")

    def depositar(self, valor):
        if self.validar_valor(valor):
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")

    def sacar(self, valor, senha):
        if senha != self.__senha:
            print("Senha incorreta.")
        elif valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")

    @classmethod
    def alterar_nome_banco(cls, novo):
        cls.banco = novo

    @staticmethod
    def validar_valor(valor):
        if valor <= 0:
            print("Erro: valor inválido.")
            return False
        return True


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo_inicial, senha, rendimento=0.03):
        super().__init__(titular, saldo_inicial, senha)
        self.rendimento = rendimento

    def sacar(self, valor, senha):
        taxa = 2
        total = valor + taxa

        if senha != self.senha:
            print("Senha incorreta.")
        elif total > self.saldo:
            print("Saldo insuficiente (com taxa de R$2).")
        else:
            self._saldo -= total
            print(f"Saque de R${valor:.2f} + taxa de R$2.00 realizado.")

    def aplicar_rendimento(self):
        ganho = self._saldo * self.rendimento
        self._saldo += ganho
        print(f"Rendimento de R${ganho:.2f} aplicado.")


# ---------------------------
# INTERFACE DE TERMINAL
# ---------------------------
def menu_conta(conta):
    while True:
        print("\n--- MENU ---")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Alterar senha")
        if isinstance(conta, ContaPoupanca):
            print("5. Aplicar rendimento")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            conta.mostrar_dados()
        elif opcao == "2":
            valor = float(input("Valor do depósito: R$"))
            conta.depositar(valor)
        elif opcao == "3":
            valor = float(input("Valor do saque: R$"))
            senha = input("Digite a senha: ")
            conta.sacar(valor, senha)
        elif opcao == "4":
            nova = input("Nova senha: ")
            conta.senha = nova
        elif opcao == "5" and isinstance(conta, ContaPoupanca):
            conta.aplicar_rendimento()
        elif opcao == "0":
            print("Saindo da conta...")
            break
        else:
            print("Opção inválida.")


# ---------------------------
# CRIAÇÃO DAS CONTAS
# ---------------------------
def main():
    print("=== Bem-vindo ao Banco Orion ===")
    nome = input("Nome do titular: ")
    saldo = float(input("Saldo inicial: R$"))
    senha = input("Crie sua senha (mínimo 4 dígitos): ")

    tipo = input("Tipo da conta [C]orrente ou [P]oupança? ").strip().upper()

    if tipo == "P":
        conta = ContaPoupanca(nome, saldo, senha)
    else:
        conta = ContaBancaria(nome, saldo, senha)

    menu_conta(conta)
    print("Obrigado por usar nosso sistema!")


# Executa o programa
if __name__ == "__main__":
    main()
