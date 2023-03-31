def calculate_S():
    S = 0
    for i in range(1, 101):
        S += 1/i
    return S

print("{:.2f}".format(calculate_S()))