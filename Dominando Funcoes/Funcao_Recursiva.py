def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(f"Fatorial de 5 é {fatorial(5)}")  # 120
