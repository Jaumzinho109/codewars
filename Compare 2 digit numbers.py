def compare(a, b):
    lista = []
    valor1 = list(str(a))
    valor2 = list(str(b))
    for v in valor1:
        if v in valor2:
            lista.append(v)
            valor2.remove(v)
        else:
            continue
    pctg = len(lista)/len(valor1) * 100
    return (f'{int(pctg)}%')

print(compare(12, 14))





