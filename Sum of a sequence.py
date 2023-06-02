def sequence_sum(begin_number, end_number, step):
    sum = 0
    for c in range(begin_number, end_number + 1, step):
        sum += c
    return sum