class ContaBancaria:
    # Variável de classe (compartilhada por TODAS as contas)
    banco = "Banco Orion"

    # Contador de contas criadas (também variável de classe)
    total_contas = 0

    def __init__(self, titular, saldo_inicial):
        # Variáveis de instância (cada conta tem seus próprios dados)
        self.titular = titular
        self.saldo = saldo_inicial

        # Incrementa o contador toda vez que uma conta é criada
        ContaBancaria.total_contas += 1

    def mostrar_dados(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")
        print(f"Banco: {ContaBancaria.banco}")  # Pode usar self.banco também


# ---------------------------
# Criando instâncias (objetos)
# ---------------------------

conta1 = ContaBancaria("Henry", 1000)
conta2 = ContaBancaria("Orion", 500)

# Mostrando dados
print("=== Conta 1 ===")
conta1.mostrar_dados()

print("\n=== Conta 2 ===")
conta2.mostrar_dados()

# Variável de classe compartilhada:
print("\nBanco (via classe):", ContaBancaria.banco)
print("Banco (via conta1):", conta1.banco)
print("Banco (via conta2):", conta2.banco)

# Alterando a variável de classe
ContaBancaria.banco = "Banco Interestelar"

print("\n=== Após mudança do nome do banco ===")
conta1.mostrar_dados()
conta2.mostrar_dados()

# Variável de classe contador
print("\nTotal de contas criadas:", ContaBancaria.total_contas)
