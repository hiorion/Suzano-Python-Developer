# Definindo a classe Bicicleta
class Bicicleta:
    # Método construtor: inicializa os atributos da bicicleta
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Método para simular a buzina da bicicleta
    def buzinar(self):
        print("Biiiii Biiiii")

    # Método para simular a bicicleta correndo
    def correr(self):
        print(f"A bicicleta {self.modelo} está correndo.")

    # Método para simular a bicicleta parando
    def parar(self):
        print(f"A bicicleta {self.modelo} parou.")

    # Método para exibir os dados da bicicleta
    def exibir_dados(self):
        print("\n--- Bicicleta Vendida ---")
        print(f"Cor: {self.cor}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Valor: R$ {self.valor:.2f}")

# Programa principal

# Criando uma instância (objeto) da classe Bicicleta
bicicleta1 = Bicicleta("Vermelha", "Speed X", 2022, 2500.00)

# Exibindo os dados da bicicleta
bicicleta1.exibir_dados()

# Executando os comportamentos da bicicleta
bicicleta1.buzinar()
bicicleta1.correr()
bicicleta1.parar()
