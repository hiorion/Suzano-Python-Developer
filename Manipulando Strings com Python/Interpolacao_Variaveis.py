# ================================
# INTERPOLAÇÃO DE VARIÁVEIS
# ================================

nome = "Maria"
idade = 30
preco = 49.9875
a = 5
b = 3
pessoa = {"nome": "Carlos", "idade": 25}

# 1. f-string (Python 3.6+): forma moderna e recomendada
print(f"1. f-string → Olá, meu nome é {nome} e tenho {idade} anos.")
# Saída esperada: Olá, meu nome é Maria e tenho 30 anos.

# 2. .format() – método antigo, ainda muito usado
print("2. format() → Olá, meu nome é {} e tenho {} anos.".format(nome, idade))
# Saída: Olá, meu nome é Maria e tenho 30 anos.

# 2b. .format() com nomes nomeados
print("2b. format(nome={n}, idade={i}) → Olá, {n}, {i} anos.".format(n=nome, i=idade))
# Saída: Olá, Maria, 30 anos.

# 3. Operador % – estilo C, menos usado atualmente
print("3. % → Olá, meu nome é %s e tenho %d anos." % (nome, idade))
# Saída: Olá, meu nome é Maria e tenho 30 anos.

# 4. f-string com formatação numérica
print(f"4. f-string com float formatado → Preço: R$ {preco:.2f}")
# Saída: Preço: R$ 49.99

# 4b. .format() com casas decimais
print("4b. format() com casas decimais → Preço: R$ {:.2f}".format(preco))
# Saída: Preço: R$ 49.99

# 5. f-string com expressões dentro das chaves
print(f"5. Expressão dentro da f-string → {a} + {b} = {a + b}")
# Saída: 5 + 3 = 8

# 6. Alinhamento e preenchimento com f-string
print(f"6a. Alinhado à direita: [{nome:>10}]")   # Espaço à esquerda
print(f"6b. Alinhado à esquerda: [{nome:<10}]")  # Espaço à direita
print(f"6c. Centralizado: [{nome:^10}]")         # Centralizado

# 7. Usando dicionários com f-string e .format()
print(f"7a. f-string com dict → {pessoa['nome']} tem {pessoa['idade']} anos.")
print("7b. format com dict → {nome} tem {idade} anos.".format(**pessoa))
