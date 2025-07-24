from abc import ABC, abstractmethod
from datetime import date


# ======================= TRANSACOES =======================
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        return conta.depositar(self.valor)


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        return conta.sacar(self.valor)


# ======================= HISTÓRICO =======================
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


# ======================= CONTA =======================
class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def saldo_atual(self):
        return self.saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        self.historico.adicionar_transacao(f"Saque de R$ {valor:.2f}")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False
        self.saldo += valor
        self.historico.adicionar_transacao(f"Depósito de R$ {valor:.2f}")
        return True


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500.0, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques excedido.")
            return False
        if valor > (self.saldo + self.limite):
            print("Limite insuficiente.")
            return False
        self.saldo -= valor
        self.saques_realizados += 1
        self.historico.adicionar_transacao(f"Saque de R$ {valor:.2f}")
        return True


# ======================= CLIENTES =======================
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        conta.historico.adicionar_transacao(transacao.__class__.__name__)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


# ======================= EXEMPLO DE USO =======================

if __name__ == "__main__":
    cliente1 = PessoaFisica("João Silva", "123.456.789-00", date(1990, 5, 20), "Rua das Flores")
    conta1 = ContaCorrente.nova_conta(cliente1, numero=1)
    cliente1.adicionar_conta(conta1)

    cliente1.realizar_transacao(conta1, Deposito(1000))
    cliente1.realizar_transacao(conta1, Saque(200))
    cliente1.realizar_transacao(conta1, Saque(900))  # Teste de limite

    print("\nTransações:")
    for t in conta1.historico.transacoes:
        print("-", t)

    print(f"\nSaldo final: R$ {conta1.saldo_atual():.2f}")
