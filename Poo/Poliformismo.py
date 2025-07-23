class ContaBancaria:
    def __init__(self, titular, saldo_inicial, senha):
        self.titular = titular
        self._saldo = saldo_inicial
        self.__senha = senha

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("Saldo não pode ser negativo.")

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) >= 4:
            self.__senha = nova_senha
            print("Senha alterada.")
        else:
            print("Senha muito curta.")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor inválido.")

    def sacar(self, valor, senha):
        if senha != self.__senha:
            print("Senha incorreta.")
        elif valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")


# -----------------------------
# Subclasse com herança + polimorfismo
# -----------------------------
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo_inicial, senha, rendimento):
        # Chama o construtor da classe base
        super().__init__(titular, saldo_inicial, senha)
        self.rendimento = rendimento  # percentual (ex: 0.03 para 3%)

    # Polimorfismo: sobrescreve o método sacar
    def sacar(self, valor, senha):
        taxa = 2  # Taxa fixa para saques da poupança
        total = valor + taxa

        if senha != self.senha:
            print("Senha incorreta.")
        elif total > self.saldo:
            print("Saldo insuficiente (taxa de R$2 aplicada).")
        else:
            self._saldo -= total
            print(f"Saque de R${valor:.2f} com taxa de R$2.00 realizado.")

    # Novo método exclusivo da poupança
    def aplicar_rendimento(self):
        ganho = self.saldo * self.rendimento
        self._saldo += ganho
        print(f"Rendimento de R${ganho:.2f} aplicado. Novo saldo: R${self.saldo:.2f}")


# -----------------------------
# Testando o código
# -----------------------------

# Conta normal
print("=== CONTA NORMAL ===")
conta1 = ContaBancaria("Henry", 1000, "1234")
conta1.depositar(200)
conta1.sacar(300, "1234")
print("Saldo final:", conta1.saldo)

# Conta poupança com polimorfismo
print("\n=== CONTA POUPANÇA ===")
conta2 = ContaPoupanca("Orion", 1000, "5678", rendimento=0.05)
conta2.depositar(500)
conta2.sacar(300, "5678")  # Vai aplicar taxa de R$2
conta2.aplicar_rendimento()
print("Saldo final da poupança:", conta2.saldo)
