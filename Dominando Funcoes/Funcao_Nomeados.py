def mostrar_info(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

mostrar_info(nome="Carlos", idade=28, cidade="São Paulo")
# Saída:
# nome: Carlos
# idade: 28
# cidade: São Paulo
