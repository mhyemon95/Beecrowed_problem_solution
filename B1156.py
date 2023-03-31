def calculate_S():
    S = 0
    for i in range(1, 40, 2):
        S += i / (2**(i//2))
    return S

print("{:.2f}".format(calculate_S()))
