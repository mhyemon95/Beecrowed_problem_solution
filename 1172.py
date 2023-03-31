x = [int(input()) for i in range(10)]
for i in range(10):
    if x[i] <= 0:
        x[i] = 1
    print("X[{}] = {}".format(i, x[i]))
