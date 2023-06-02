def find_missing(sequence):
    # Valor recebe a soma dos valores de uma PA
    # soma_lista recebe a soma dos valores da lista em questão
    # num_faltante é o valor que está faltando na lista em questão para que ela seja uma PA
    valor_soma = (sequence[0] + sequence[-1]) * (len(sequence)+1)/2
    soma_lista = 0
    for v in sequence:
        soma_lista += v
    num_faltante = valor_soma - soma_lista
    return num_faltante

x = [2, 4, 6, 8, 10, 14, 16]
y = find_missing(x)
print(y)