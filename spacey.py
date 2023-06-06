def spacey(array):
    pronto = []
    novo = ''
    for k, v in enumerate(array):
        if k == 0:
            pronto.append(v)
        else:
            novo = pronto[k - 1] + v
            pronto.append(novo)
    return pronto
print(spacey(['I', 'dont','have','space']))