class ContaBancaria:
    # VARIÁVEIS DE CLASSE (compartilhadas por todas as instâncias)
    banco = "Banco Orion"
    total_contas = 0

    def __init__(self, titular, saldo_inicial, senha):
        # VARIÁVEIS DE INSTÂNCIA (exclusivas de cada objeto)
        self.titular = titular
        self._saldo = saldo_inicial
        self.__senha = senha

        # Incrementa contador de contas
        ContaBancaria.total_contas += 1

    # PROPRIEDADE: Getter e Setter do saldo
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("Erro: saldo não pode ser negativo.")

    # PROPRIEDADE: Getter e Setter da senha (somente para fins didáticos)
    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) >= 4:
            self.__senha = nova_senha
            print("Senha alterada com sucesso.")
        else:
            print("Erro: senha muito curta.")

    # MÉTODO DE INSTÂNCIA: Acessa dados da instância
    def mostrar_dados(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self._saldo:.2f}")
        print(f"Banco: {ContaBancaria.banco}")

    def depositar(self, valor):
        if ContaBancaria.validar_valor(valor):
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

    # MÉTODO DE CLASSE: Acessa/Modifica atributos da classe
    @classmethod
    def alterar_nome_banco(cls, novo_nome):
        cls.banco = novo_nome
        print(f"Nome do banco alterado para: {cls.banco}")

    # MÉTODO ESTÁTICO: Função auxiliar, sem acesso a self nem cls
    @staticmethod
    def validar_valor(valor):
        if valor <= 0:
            print("Erro: valor deve ser positivo.")
            return False
        return True


# SUBCLASSE: Herança + Polimorfismo
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo_inicial, senha, rendimento):
        super().__init__(titular, saldo_inicial, senha)
        self.rendimento = rendimento  # Ex: 0.05 = 5%

    # POLIMORFISMO: sobrescrevendo método sacar com taxa
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

    # Método exclusivo da subclasse
    def aplicar_rendimento(self):
        ganho = self._saldo * self.rendimento
        self._saldo += ganho
        print(f"Rendimento de R${ganho:.2f} aplicado. Novo saldo: R${self._saldo:.2f}")


# -----------------------------
# TESTANDO O SISTEMA
# -----------------------------

print("=== CONTA NORMAL ===")
conta1 = ContaBancaria("Henry", 1000, "1234")
conta1.mostrar_dados()
conta1.depositar(500)
conta1.sacar(300, "1234")
conta1.mostrar_dados()

print("\n=== CONTA POUPANÇA ===")
conta2 = ContaPoupanca("Orion", 2000, "5678", rendimento=0.05)
conta2.mostrar_dados()
conta2.depositar(1000)
conta2.sacar(500, "5678")  # aplica taxa de R$2
conta2.aplicar_rendimento()
conta2.mostrar_dados()

print("\n=== ALTERANDO DADOS COMPARTILHADOS ===")
ContaBancaria.alterar_nome_banco("Banco Interestelar")
conta1.mostrar_dados()
conta2.mostrar_dados()

print("\n=== TOTAL DE CONTAS CRIADAS ===")
print("Total:", ContaBancaria.total_contas)

print("\n=== VALIDAÇÃO COM MÉTODO ESTÁTICO ===")
ContaBancaria.validar_valor(-10)
ContaBancaria.validar_valor(100)
