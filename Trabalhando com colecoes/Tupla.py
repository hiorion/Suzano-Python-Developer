# ============================
# Tuplas em Python
# ============================

# Criando tuplas
tupla_vazia = ()
tupla_numeros = (1, 2, 3, 4, 5)
tupla_mista = ("Alice", 30, True, 7.5)

print("Tuplas criadas:")
print("Vazia:", tupla_vazia)
print("Números:", tupla_numeros)
print("Mista:", tupla_mista)
print()

# Acessando elementos
print("Acessando elementos:")
print("Primeiro elemento:", tupla_numeros[0])
print("Último elemento:", tupla_numeros[-1])
print()

# Percorrendo tupla com for
print("Percorrendo tupla_numeros:")
for numero in tupla_numeros:
    print("-", numero)
print()

# Tamanho da tupla
print("Tamanho da tupla_mista:", len(tupla_mista))
print()

# Verificando existência
if 3 in tupla_numeros:
    print("O número 3 está na tupla.")
else:
    print("O número 3 não está na tupla.")
print()

# Métodos disponíveis
tupla_exemplo = (1, 2, 2, 3, 4, 2)
print("Tupla exemplo:", tupla_exemplo)
print("Quantidade de vezes que 2 aparece:", tupla_exemplo.count(2))
print("Índice da primeira ocorrência do número 3:", tupla_exemplo.index(3))
print()

# Tupla com um único elemento (necessário usar vírgula)
tupla_unico = (42,)
print("Tupla com um único elemento:", tupla_unico)
print("Tipo:", type(tupla_unico))
print()

# Conversão entre lista e tupla
lista = [10, 20, 30]
tupla_convertida = tuple(lista)
print("Lista convertida em tupla:", tupla_convertida)

lista_convertida = list(tupla_numeros)
print("Tupla convertida em lista:", lista_convertida)
