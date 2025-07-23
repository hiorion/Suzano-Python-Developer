class ContaBancaria:
    def __init__(self, titular, saldo_inicial, senha):
        # Atributo público
        self.titular = titular

        # Atributo protegido (por convenção)
        self._saldo = saldo_inicial

        # Atributo privado (name mangling)
        self.__senha = senha

    # ----------------------
    # PROPRIEDADE SALDO
    # ----------------------
    @property
    def saldo(self):
        """Getter do saldo (somente leitura externa)"""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """Setter do saldo com validação"""
        if valor >= 0:
            self._saldo = valor
        else:
            print("Erro: saldo não pode ser negativo.")

    # ----------------------
    # PROPRIEDADE SENHA
    # ----------------------
    @property
    def senha(self):
        """Getter da senha (somente para exemplo)"""
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        """Setter da senha com validação"""
        if len(nova_senha) >= 4:
            self.__senha = nova_senha
            print("Senha alterada com sucesso.")
        else:
            print("Erro: senha muito curta.")

    # ----------------------
    # MÉTODO DE DEPÓSITO
    # ----------------------
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Erro: valor de depósito inválido.")

    # ----------------------
    # MÉTODO DE SAQUE
    # ----------------------
    def sacar(self, valor, senha):
        if senha != self.__senha:
            print("Erro: senha incorreta.")
        elif valor > self._saldo:
            print("Erro: saldo insuficiente.")
        else:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")


# -----------------------------
# USO PRÁTICO DO OBJETO
# -----------------------------

# Criando uma conta
conta = ContaBancaria("Henry", 1000, "1234")

# Acessando atributo público
print("Titular:", conta.titular)

# Lendo saldo via propriedade
print("Saldo inicial:", conta.saldo)

# Depositando
conta.depositar(500)
print("Saldo após depósito:", conta.saldo)

# Tentando sacar com senha incorreta
conta.sacar(200, "0000")

# Sacando com senha correta
conta.sacar(200, "1234")
print("Saldo após saque:", conta.saldo)

# Ajustando saldo diretamente via propriedade (setter)
conta.saldo = 1500
print("Saldo ajustado manualmente:", conta.saldo)

# Tentando saldo negativo
conta.saldo = -300  # Não será aceito

# Lendo senha (não recomendado em sistemas reais)
print("Senha atual:", conta.senha)

# Alterando senha via propriedade
conta.senha = "5678"

# Testando novo saque com nova senha
conta.sacar(100, "5678")
print("Saldo final:", conta.saldo)
