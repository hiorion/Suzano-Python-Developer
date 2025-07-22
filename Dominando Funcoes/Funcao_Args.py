def soma_todos(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(f"Soma de 1,2,3,4 = {soma_todos(1, 2, 3, 4)}")  # 10
print(f"Soma de 5,10 = {soma_todos(5, 10)}")          # 15
