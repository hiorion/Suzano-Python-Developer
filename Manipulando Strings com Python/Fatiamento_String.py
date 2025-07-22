# ========================
# FATIAMENTO DE STRINGS
# ========================

texto = "Python é incrível"

# 1. Pegar caracteres do índice 0 até 5 (exclusivo o 6)
print("1. texto[0:6] →", texto[0:6])  
# Saída: Python (letras do índice 0 até 5)

# 2. Pegar do início até o índice 5
print("2. texto[:6] →", texto[:6])  
# Saída: Python (mesmo que acima)

# 3. Pegar do índice 7 até o final
print("3. texto[7:] →", texto[7:])  
# Saída: é incrível

# 4. Pegar toda a string
print("4. texto[:] →", texto[:])  
# Saída: Python é incrível

# 5. Pegar do índice 0 até o fim, pulando 2 caracteres
print("5. texto[0::2] →", texto[0::2])  
# Saída: Ptoécnívl (letras pulando 1 a 1)

# 6. Pegar do índice 1 até o fim, pulando 3 caracteres
print("6. texto[1::3] →", texto[1::3])  
# Saída: y  r (exemplo de salto 3 em 3)

# 7. Pegar os últimos 8 caracteres
print("7. texto[-8:] →", texto[-8:])  
# Saída: incrível

# 8. Pegar do índice -8 até -1
print("8. texto[-8:-1] →", texto[-8:-1])  
# Saída: incríve

# 9. Inverter a string inteira
print("9. texto[::-1] →", texto[::-1])  
# Saída: elbírcni é nohtyP

# 10. Inverter uma parte da string (do índice 0 até 6)
print("10. texto[0:6][::-1] →", texto[0:6][::-1])  
# Saída: nohtyP

# 11. Pegar uma substring do meio (índices 7 a 9)
print("11. texto[7:10] →", texto[7:10])  
# Saída: é i

# 12. Pular um caractere começando do índice 2 até 10
print("12. texto[2:11:2] →", texto[2:11:2])  
# Saída: to é

