# Classe base Animal
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def mover(self):
        print(f"{self.nome} está se movendo.")

# Classe Mamífero herda de Animal
class Mamifero(Animal):
    def amamentar(self):
        print(f"{self.nome} está amamentando.")

# Classe Ave herda de Animal
class Ave(Animal):
    def voar(self):
        print(f"{self.nome} está voando.")

# Classe Cachorro herda de Mamífero
class Cachorro(Mamifero):
    def latir(self):
        print(f"{self.nome} está latindo.")

# Classe Gato herda de Mamífero
class Gato(Mamifero):
    def miar(self):
        print(f"{self.nome} está miando.")

# Classe Leão herda de Mamífero
class Leao(Mamifero):
    def rugir(self):
        print(f"{self.nome} está rugindo.")

# Classe Ornitorrinco herda de Mamífero e Ave (herança múltipla)
class Ornitorrinco(Mamifero, Ave):
    def botar_ovos(self):
        print(f"{self.nome} está botando ovos.")

# Testando os objetos

print("=== Cachorro ===")
cachorro = Cachorro("Bob")
cachorro.mover()
cachorro.amamentar()
cachorro.latir()

print("\n=== Gato ===")
gato = Gato("Mimi")
gato.mover()
gato.amamentar()
gato.miar()

print("\n=== Leão ===")
leao = Leao("Simba")
leao.mover()
leao.amamentar()
leao.rugir()

print("\n=== Ornitorrinco ===")
ornitorrinco = Ornitorrinco("Perry")
ornitorrinco.mover()
ornitorrinco.amamentar()
ornitorrinco.voar()
ornitorrinco.botar_ovos()
