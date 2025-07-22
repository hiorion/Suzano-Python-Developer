# ================================
# MÉTODOS CLASSE DE STRING
# ================================

texto = "  Olá, Mundo Python!  "
nome = "ana maria"
codigo = "42"
frutas = "maçã,banana,uva"

# 1. strip() – remove espaços dos dois lados
print("1. strip() →", texto.strip())  # "Olá, Mundo Python!"

# 2. lower() – tudo minúsculo
print("2. lower() →", texto.lower())  # "  olá, mundo python!  "

# 3. upper() – tudo MAIÚSCULO
print("3. upper() →", texto.upper())  # "  OLÁ, MUNDO PYTHON!  "

# 4. capitalize() – primeira letra maiúscula
print("4. capitalize() →", nome.capitalize())  # "Ana maria"

# 5. title() – primeira letra de cada palavra maiúscula
print("5. title() →", nome.title())  # "Ana Maria"

# 6. replace("antigo", "novo") – substitui trecho
print("6. replace('Python', 'Java') →", texto.replace("Python", "Java"))  # "  Olá, Mundo Java!  "

# 7. split(',') – divide a string em lista
print("7. split(',') →", frutas.split(","))  # ['maçã', 'banana', 'uva']

# 8. join() – junta lista em uma string
lista = ["João", "Maria", "Pedro"]
print("8. join(lista) →", ", ".join(lista))  # "João, Maria, Pedro"

# 9. find("sub") – encontra a posição da substring
print("9. find('Mundo') →", texto.find("Mundo"))  # 7 (posição inicial)

# 10. in – verifica se contém
print("10. 'Python' in texto →", "Python" in texto)  # True

# 11. count("a") – conta quantas vezes aparece
print("11. count('a') →", nome.count("a"))  # 3

# 12. startswith("prefixo") – começa com
print("12. startswith('  Olá') →", texto.startswith("  Olá"))  # True

# 13. endswith("Python!  ") – termina com
print("13. endswith('Python!  ') →", texto.endswith("Python!  "))  # True

# 14. zfill(5) – preenche com zeros à esquerda
print("14. zfill(5) →", codigo.zfill(5))  # "00042"

# 15. isdigit() – verifica se é numérico
print("15. '123'.isdigit() →", "123".isdigit())  # True

# 16. isalpha() – só letras
print("16. 'abc'.isalpha() →", "abc".isalpha())  # True

# 17. isalnum() – letras e números
print("17. 'abc123'.isalnum() →", "abc123".isalnum())  # True

# 18. isspace() – só espaços
print("18. '   '.isspace() →", "   ".isspace())  # True

# 19. swapcase() – inverte maiúsculas e minúsculas
print("19. swapcase() →", "PyThOn".swapcase())  # "pYtHoN"

# 20. Inverter string com fatiamento
print("20. texto[::-1] →", texto[::-1])  # string invertida
