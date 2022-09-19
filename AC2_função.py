# Crie um programa que solicite ao usuário o nome e
# o número de cinco candidatos que concorrerão à uma
# eleição, o número deve ser único para cada candidato e
# serão válidos apenas números naturais.
# Em seguida, peça os votos de cada pessoa para que possam
# ser contabilizados, o voto será mediante o número do
# candidato.
# Ao final, o programa deverá exibir o nome dos candidatos,
# e a quantidade de votos, inclusive os votos em branco.
# O programa também deverá exibir o vencedor da eleição.
# Obs.(1): O programa deve prever a situação em que o usuário
#          tente votar em um candidato inexistente, nesse caso
#          o voto será anulado. Uma mensagem deverá ser exibida
#          indicando o ocorrido.
# Obs.(2): Caso o usuário digite o número de voto -1, isso indicará
#          um voto em branco. Uma mensagem deverá ser exibida
#          indicando o ocorrido.
# Obs.(3): Após a confirmação de um voto válido, o programa deverá
#          exibir o nome do candidato que recebeu o voto.
# Obs.(4): O programa deve registrar os números dos candidatos, os
#          nomes e a quantidade de votos em um dicionário, isto é,
#          o número deverá ser a chave e o valor associado uma lista
#          em que o primeiro valor é o nome e o segundo a quantidade
#          de votos.
# Obs.(5): O seu código de resposta deve estar logo em seguida deste
#          enunciado, ou seja, faça o download deste arquivo, insira
#          o seu código abaixo e anexe novamente o arquivo como resposta.

def verifica_numero_candidato(dicionario, lista_candidato, num_voto, lista_votos):
    i = 0
    for _ in range(5):
        if dicionario[lista_candidato[i]] == int(num_voto):
            lista_votos.append(num_voto)
            print(lista_candidato[i])
        i += 1

presidentes_fofinhos = dict()

for _ in range(5):
    nome_candidato = input()
    num_candidato = int(input())
    presidentes_fofinhos[nome_candidato] = num_candidato

lista_votos = []
candidatos = list(presidentes_fofinhos.keys())
num_candidatos = list(presidentes_fofinhos.values())

while True:
    voto =  input()
    if str(voto) == "ACABOU" or str(voto) == "acabou":
        break
    elif int(voto) < 0:
        print("Voto em Branco!")
    elif int(voto) not in presidentes_fofinhos.values():
        print("Voto Anulado!")
    else:
        verifica_numero_candidato(presidentes_fofinhos, candidatos, voto, lista_votos)

i = 0
for __ in range(5):
    print(f"{candidatos[i]}: {lista_votos.count(f'{presidentes_fofinhos[candidatos[i]]}')} voto(s)")
    i += 1