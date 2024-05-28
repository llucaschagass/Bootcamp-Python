capacidade_atual, aumento_percentual = map(int, input().split())

# Calculando a nova capacidade do disco de Mithril
nova_capacidade = capacidade_atual * (1 + aumento_percentual / 100)

# Imprimindo a nova capacidade
print(int(nova_capacidade))