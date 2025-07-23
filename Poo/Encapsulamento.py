class ContaBancaria:
    def __init__(self, titular, saldo_inicial, senha):
        # Atributo público
        self.titular = titular

        # Atributo protegido (uso interno por convenção)
        self._saldo = saldo_inicial

        # Atributo privado (realmente "escondido" da classe)
        self.__senha = senha

    # Método público para mostrar saldo (getter)
    def get_saldo(self):
        return self._saldo

    # Método público para depositar dinheiro (setter com validação)
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor} realizado.")
        else:
            print("Valor inválido para depósito.")

    # Método público para sacar dinheiro (com validação)
    def sacar(self, valor, senha):
        if senha != self.__senha:
            print("Senha incorreta!")
        elif valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
            print(f"Saque de R${valor} realizado.")

    # Getter da senha (apenas exemplo, não recomendado expor senha)
    def get_senha(self):
        return self.__senha

    # Setter da senha (com validação)
    def set_senha(self, nova_senha):
        if len(nova_senha) >= 4:
            self.__senha = nova_senha
            print("Senha alterada com sucesso.")
        else:
            print("Senha muito curta.")


# ---------------------
# USO DO OBJETO
# ---------------------

# Criar uma conta
conta = ContaBancaria("Henry", 1000, "1234")

# Acessar atributo público
print("Titular da conta:", conta.titular)

# Acessar saldo com método getter
print("Saldo atual:", conta.get_saldo())

# Fazer um depósito
conta.depositar(500)
print("Saldo após depósito:", conta.get_saldo())

# Tentar sacar com senha errada
conta.sacar(200, "0000")  # Senha errada

# Sacar com senha correta
conta.sacar(200, "1234")
print("Saldo após saque:", conta.get_saldo())

# Trocar a senha
conta.set_senha("5678")

# Verificando a senha (só por exemplo)
print("Senha atual (via método):", conta.get_senha())

# Tentando acessar diretamente o atributo privado (vai dar erro)
# print(conta.__senha)  # → AttributeError

# Acessar forçadamente com name mangling (NÃO recomendado)
print("Senha via name mangling:", conta._ContaBancaria__senha)
