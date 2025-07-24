# Primeira classe base
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}.")

# Segunda classe base
class Funcionario:
    def __init__(self, cargo):
        self.cargo = cargo

    def trabalhar(self):
        print(f"Trabalhando como {self.cargo}.")

# Classe que herda de Pessoa e Funcionario
class Professor(Pessoa, Funcionario):
    def __init__(self, nome, cargo, disciplina):
        Pessoa.__init__(self, nome)      # Chamando explicitamente o construtor de Pessoa
        Funcionario.__init__(self, cargo)  # Chamando explicitamente o construtor de Funcionario
        self.disciplina = disciplina

    def lecionar(self):
        print(f"{self.nome} está lecionando {self.disciplina}.")

# Criando um objeto da classe Professor
prof = Professor("João", "Professor", "Matemática")
prof.apresentar()
prof.trabalhar()
prof.lecionar()
