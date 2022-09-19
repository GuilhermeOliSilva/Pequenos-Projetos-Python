lista_noivo = set()
lista_noiva = set()

while True:
    convidado = input().split(";")
    if convidado[0] == "ACABOU":
        lista_noivo.discard("noivo")
        lista_noiva.discard("noiva")
        break
    elif convidado[1] == "noivo":
        lista_noivo.update(convidado)
    elif convidado[1] == "noiva":
        lista_noiva.update(convidado)

lista_uniao = lista_noivo | lista_noiva
lista_interseccao = lista_noivo & lista_noiva
lista_diferenca_simetrica = lista_noivo ^ lista_noiva

print("-" * 20)
print("LISTA FINAL")
print("-" * 20)
for item in sorted(lista_uniao):
    print(item)

print("\n" + "-" * 20)
print("APENAS NOIVA")
print("-" * 20)
for item in sorted(lista_noiva):
    if item in lista_noivo:
        continue
    print(item)

print("\n" + "-" * 20)
print("APENAS NOIVO")
print("-" * 20)
for item in sorted(lista_noivo):
    if item in lista_noiva:
        continue
    print(item)

print("\n" + "-" * 20)
print("POR AMBOS")
print("-" * 20)
for item in sorted(lista_interseccao):
    print(item)

print("\n" + "-" * 20)
print("POR APENAS UM DELES")
print("-" * 20)
for item in sorted(lista_diferenca_simetrica):
    print(item)