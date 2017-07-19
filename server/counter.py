def counter(count_data):
    z = 0
    x = len(count_data)
    for i in range(x):
        y = len(count_data[i])
        z = z + y
    return z
