# ============================
# Conjuntos em Python
# ============================

# Criando conjuntos
conjunto_vazio = set()  # Usar set(), pois {} cria um dicionário
conjunto_numeros = {1, 2, 3, 4, 5}
conjunto_repetidos = {1, 2, 2, 3, 3, 4}

print("Conjuntos criados:")
print("Vazio:", conjunto_vazio)
print("Números:", conjunto_numeros)
print("Com repetidos (elimina duplicatas automaticamente):", conjunto_repetidos)
print()

# Adicionando elementos
conjunto_numeros.add(6)
print("Após adicionar 6:", conjunto_numeros)

# Removendo elementos
conjunto_numeros.remove(3)  # Remove 3, dá erro se não existir
print("Após remover 3:", conjunto_numeros)

conjunto_numeros.discard(10)  # Não dá erro se 10 não existir
print("Após tentar descartar 10 (sem erro):", conjunto_numeros)
print()

# Verificando existência
if 4 in conjunto_numeros:
    print("O número 4 está no conjunto.")
else:
    print("O número 4 não está no conjunto.")
print()

# Operações de conjuntos
pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7}
misturados = {1, 2, 3, 4}

print("União:", pares.union(impares))               # Todos os elementos
print("Interseção:", pares.intersection(misturados))  # Elementos em comum
print("Diferença (pares - misturados):", pares.difference(misturados))  # Apenas em pares
print("Diferença simétrica:", pares.symmetric_difference(misturados))  # Elementos exclusivos
print()

# Conversão de lista para conjunto
lista_com_repetidos = [1, 2, 2, 3, 4, 4, 5]
conjunto_unico = set(lista_com_repetidos)
print("Lista com repetidos:", lista_com_repetidos)
print("Convertida em conjunto (sem duplicatas):", conjunto_unico)
