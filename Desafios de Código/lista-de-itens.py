# Lista para armazenar os itens
itens = []

# Solicitando os itens ao usuário
for i in range(3):
    item = input()
    itens.append(item)

# Exibindo a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")