numero_itens = 0
itens = []
produtos = ""
while numero_itens <= 2:
    produtos = input()
    itens.append(produtos)
    numero_itens += 1
print("Lista")
for item in itens:
    print(f"- {item}")