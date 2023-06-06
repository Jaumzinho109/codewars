def alternate(n, first_value, second_value):
    arr = []
    while True: 
        if n != 0:
            arr.append(first_value)
        else:
            break
        n -= 1
        if n != 0:
            arr.append(second_value)
        else:
            break
        n -= 1
    return arr
print(alternate(5, True, False))