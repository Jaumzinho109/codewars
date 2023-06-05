def strings_construction(a, b):
    count = 0
    copia = list(a)[:]
    for v in list(b):
        if v in copia:
            copia.remove(v)
            if copia == []:
                count += 1
                copia = list(a)[:]
        else:
            continue
    return count

print(strings_construction('bcyc', 'cgcgylqycdqlvbowcchgibcbthyd'))
