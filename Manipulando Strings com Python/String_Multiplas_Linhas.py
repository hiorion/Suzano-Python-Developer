# =============================
# STRINGS DE MÚLTIPLAS LINHAS
# =============================

# 1. String com aspas triplas (""")
texto_multilinhas = """Essa é uma string
que ocupa várias linhas,
mantendo a formatação
exatamente como foi escrita."""

print("1. String com aspas triplas:")
print(texto_multilinhas)
print("-" * 40)

# 2. String com aspas triplas simples (''')
texto_multilinhas2 = '''Também funciona
com aspas simples triplas,
mantendo múltiplas linhas.'''

print("2. String com aspas triplas simples:")
print(texto_multilinhas2)
print("-" * 40)

# 3. Quebrar linhas com \n dentro de aspas simples ou duplas
texto_com_quebra = "Linha 1\nLinha 2\nLinha 3"

print("3. String com \\n para nova linha:")
print(texto_com_quebra)
print("-" * 40)

# 4. Mantendo indentação em strings multilinhas
texto_indentado = """
    Linha 1 com indentação
    Linha 2 também indentada
"""

print("4. String multilinhas com indentação preservada:")
print(texto_indentado)
print("-" * 40)

# 5. Exemplo com strip() para remover espaços em excesso no início e fim
print("5. String multilinhas com strip():")
print(texto_indentado.strip())
