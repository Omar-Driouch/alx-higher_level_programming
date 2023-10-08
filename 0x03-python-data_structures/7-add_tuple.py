def add_tuple(tuple_a=(), tuple_b=()):
    result = ()

    min_len = min(len(tuple_a), len(tuple_b))

    for i in range(min_len):
        sum = tuple_a[i] + tuple_b[i]
        result += (sum,)

    if len(tuple_a) > min_len:
        result += tuple_a[min_len:]
    elif len(tuple_b) > min_len:
        result += tuple_b[min_len:]

    return (result)
