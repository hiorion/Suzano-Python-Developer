# Definindo a classe ContaBancaria
class ContaBancaria:
    # Método construtor, executado ao criar um novo objeto
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente  # Atributo do cliente (nome)
        self.saldo = saldo      # Atributo do saldo, com valor inicial padrão igual a 0

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        self.saldo += valor  # Soma o valor ao saldo atual
        print(f"Depósito de R$ {valor:.2f} realizado.")  # Mostra mensagem de confirmação

    # Método para sacar dinheiro da conta
    def sacar(self, valor):
        # Verifica se o valor de saque é menor ou igual ao saldo disponível
        if valor <= self.saldo:
            self.saldo -= valor  # Subtrai o valor do saldo
            print(f"Saque de R$ {valor:.2f} realizado.")  # Confirmação do saque
        else:
            print("Saldo insuficiente.")  # Mensagem de erro se o saldo for menor

    # Método para exibir o extrato da conta (saldo atual)
    def extrato(self):
        print(f"Cliente: {self.cliente}")  # Mostra o nome do cliente
        print(f"Saldo atual: R$ {self.saldo:.2f}")  # Mostra o saldo da conta

# ============================
# Criando um objeto (instância) da classe ContaBancaria
conta1 = ContaBancaria("Henry")  # Cria uma conta para o cliente "Henry" com saldo padrão (0)

# Realizando operações
conta1.depositar(1000)  # Depósito de R$ 1000
conta1.sacar(200)       # Saque de R$ 200
conta1.extrato()        # Exibe o extrato da conta
