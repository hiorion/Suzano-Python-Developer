from abc import ABC, abstractmethod

# Classe abstrata
class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def fazer_som(self):
        pass  # Subclasses devem implementar

    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e sou um {self.__class__.__name__}.")


# Subclasse 1
class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")


# Subclasse 2
class Gato(Animal):
    def fazer_som(self):
        print("Miau!")


# Subclasse 3
class Vaca(Animal):
    def fazer_som(self):
        print("Muuuu!")


# Teste do polimorfismo
def interagir_com_animal(animal: Animal):
    animal.apresentar()
    animal.fazer_som()


# Execução
animais = [
    Cachorro("Bob"),
    Gato("Mimi"),
    Vaca("Mimosa")
]

for animal in animais:
    interagir_com_animal(animal)
