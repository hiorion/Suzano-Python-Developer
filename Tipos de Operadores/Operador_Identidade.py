# 5. OPERADORES DE IDENTIDADE
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)         # True – mesmos objetos na memória
print("a is c:", a is c)         # False – mesmo conteúdo, objetos diferentes
print("a is not c:", a is not c) # True – objetos diferentes

print("\n---\n")