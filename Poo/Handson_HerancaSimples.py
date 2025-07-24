# Classe base
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"{self.marca} {self.modelo} está ligado.")

    def desligar(self):
        print(f"{self.marca} {self.modelo} está desligado.")

    def buzinar(self):
        print(f"{self.marca} {self.modelo} está buzinando: Biiiii!")

# Subclasse Motocicleta herda de Veiculo
class Motocicleta(Veiculo):
    def empinar(self):
        print(f"{self.marca} {self.modelo} está empinando.")

# Subclasse Carro herda de Veiculo
class Carro(Veiculo):
    def abrir_porta_malas(self):
        print(f"{self.marca} {self.modelo} abriu o porta-malas.")

# Subclasse Caminhao herda de Veiculo
class Caminhao(Veiculo):
    def carregar(self):
        print(f"{self.marca} {self.modelo} está sendo carregado.")

# Criando objetos de cada classe
moto = Motocicleta("Honda", "CG 160")
carro = Carro("Toyota", "Corolla")
caminhao = Caminhao("Volvo", "FH 540")

# Testando comportamentos herdados e específicos
moto.ligar()
moto.buzinar()
moto.empinar()

print()

carro.ligar()
carro.abrir_porta_malas()

print()

caminhao.ligar()
caminhao.carregar()
