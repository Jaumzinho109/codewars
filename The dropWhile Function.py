def drop_while(arr, pred):
    lista_pronta = []
    is_dropping = True

    for k, v in enumerate(arr):
        if is_dropping and pred(v):
            continue
        else:
            is_dropping = False
            lista_pronta.append(v)

    return lista_pronta



is_even=lambda n: not n%2
is_odd=lambda n: n%2
print(drop_while([2,6,4,10,1,5,4,3], is_even))