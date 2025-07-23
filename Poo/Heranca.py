# Classe base (superclasse)
class Veiculo:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

    def ligar(self):
        print(f"{self.modelo} está ligado.")

    def desligar(self):
        print(f"{self.modelo} está desligado.")

# Classe filha (subclasse) herdando de Veiculo
class Bicicleta(Veiculo):
    def __init__(self, cor, modelo, marchas):
        # Chama o construtor da classe pai
        super().__init__(cor, modelo)
        self.marchas = marchas

    def pedalar(self):
        print(f"{self.modelo} está pedalando com {self.marchas} marchas.")

# Criando uma instância da classe Bicicleta
bike = Bicicleta("vermelha", "Caloi Elite", 21)

# Acessando métodos herdados da superclasse
bike.ligar()
bike.pedalar()
bike.desligar()
