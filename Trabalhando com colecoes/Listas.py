# ============================
# Listas em Python
# ============================

# Criando listas
numeros = [10, 20, 30, 40]
nomes = ["Ana", "Bruno", "Carlos"]
dados = ["Henrique", 25, True]

print("Listas criadas:")
print("numeros:", numeros)
print("nomes:", nomes)
print("dados:", dados)
print()

# Acessando elementos
print("Acessando elementos:")
print("Primeiro nome:", nomes[0])
print("Último número:", numeros[-1])
print()

# Alterando elementos
nomes[1] = "Beatriz"
print("Alterando nome 'Bruno' para 'Beatriz':", nomes)
print()

# Adicionando elementos
nomes.append("Daniel")
print("Adicionando 'Daniel' ao final:", nomes)

nomes.insert(1, "Lucas")
print("Inserindo 'Lucas' na posição 1:", nomes)
print()

# Removendo elementos
nomes.remove("Ana")
print("Removendo 'Ana':", nomes)

nomes.pop()
print("Removendo o último elemento:", nomes)

del nomes[0]
print("Removendo o primeiro elemento com del:", nomes)
print()

# Tamanho da lista
print("Tamanho da lista nomes:", len(nomes))
print()

# Percorrendo a lista
print("Percorrendo a lista nomes:")
for nome in nomes:
    print("-", nome)
print()

# Verificando existência
if "Carlos" in nomes:
    print("Carlos está na lista")
else:
    print("Carlos não está na lista")
print()

# Ordenando lista de números
print("Lista de números antes da ordenação:", numeros)
numeros.sort()
print("Ordenada crescente:", numeros)

numeros.sort(reverse=True)
print("Ordenada decrescente:", numeros)
print()

# Copiando listas
nova_lista = numeros.copy()
print("Cópia da lista de números:", nova_lista)

# Limpando a lista
numeros.clear()
print("Lista de números após limpar:", numeros)
