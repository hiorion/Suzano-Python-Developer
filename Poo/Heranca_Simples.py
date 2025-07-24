# Classe base (superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} emite um som.")

# Classe filha (subclasse)
class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo: Au Au!")

# Criando um objeto da classe Cachorro
dog = Cachorro("Rex")
dog.emitir_som()  # Método herdado da classe Animal
dog.latir()       # Método específico da classe Cachorro
