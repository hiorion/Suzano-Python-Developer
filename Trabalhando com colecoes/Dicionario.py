# ============================
# Dicionários em Python
# ============================

# Criando um dicionário
pessoa = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}

print("Dicionário original:")
print(pessoa)
print()

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print()

# Adicionando novos pares chave-valor
pessoa["profissao"] = "Engenheira"
print("Após adicionar profissão:")
print(pessoa)
print()

# Modificando valores existentes
pessoa["idade"] = 31
print("Após atualizar idade:")
print(pessoa)
print()

# Removendo uma chave
del pessoa["cidade"]
print("Após remover cidade:")
print(pessoa)
print()

# Usando o método get() (evita erro se a chave não existir)
print("Telefone (com get):", pessoa.get("telefone", "Não informado"))
print()

# Iterando sobre o dicionário
print("Chaves e valores:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
print()

# Verificando se uma chave existe
if "nome" in pessoa:
    print("A chave 'nome' existe no dicionário.")
print()

# Obtendo apenas chaves ou apenas valores
print("Todas as chaves:", list(pessoa.keys()))
print("Todos os valores:", list(pessoa.values()))
print()

# Limpando o dicionário
pessoa.clear()
print("Dicionário após clear():", pessoa)
