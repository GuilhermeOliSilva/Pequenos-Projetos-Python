qtd_info = int(input("Quantidade de informações: "))
lista = []

for i in range(qtd_info):
    registros_tabelas = input("Registro: ").split(";") #1-nomeCanal, 2-qtd_inscritos, 3-moneyMouth, 4-booleanpremeium
    lista.append(registros_tabelas)

#mil inscritos a mais no canal
x = float(input("Bônus com premium: ")) #possui premium
y = float(input("Bônus sem premium: ")) #não possui premium

print(5 * "-")
print("BÔNUS")
print(5 * "-")

nome = 0
inscritos = 0
recebe = 0

for j in range(qtd_info):
    if lista[nome][3] == "sim":
        bonus1 = ((float(lista[inscritos][1]) / 1000) * x) + float(lista[recebe][2])
        print(f"{lista[nome][0]}: R$ {bonus1:.2f}")
    else:
        bonus2 = ((float(lista[inscritos][1]) / 1000) * y) + float(lista[recebe][2])
        print(f"{lista[nome][0]}: R$ {bonus2:.2f}")
    nome += 1
    inscritos += 1
    recebe += 1