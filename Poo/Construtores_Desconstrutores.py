class Bicicleta:
    # Construtor: é chamado automaticamente ao criar o objeto
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        print(f"Bicicleta {self.modelo} criada com sucesso.")

    # Método de exibição
    def exibir(self):
        print(f"Bicicleta - Cor: {self.cor} | Modelo: {self.modelo}")

    # Desconstrutor: é chamado quando o objeto é destruído (ou o programa termina)
    def __del__(self):
        print(f"Bicicleta {self.modelo} removida da memória.")

# Criando o objeto bicicleta
b1 = Bicicleta("Azul", "Speed")

# Chamando um método
b1.exibir()

# Forçando a exclusão do objeto (desencadeia o método __del__)
del b1

# Se tentar usar b1 depois daqui, dará erro, pois foi deletado
