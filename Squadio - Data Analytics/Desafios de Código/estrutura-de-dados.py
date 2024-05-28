# Desafios Python: Organizando seus Ativos

ativos = []

# Entrada da quantidade de ativos

quantidadeAtivos = int(input())

for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# Ordenar os ativos em ordem alfabética.

ativos.sort()

# Imprimir a lista de ativos ordenada.

for item in ativos:
    print(item)