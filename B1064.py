c = 0
avg = 0
for i in range(6):
    n = float(input())
    if n > 0.0:
        c += 1
        avg += n
print(c,"valores positivos")
print("{:.1f}".format(avg/c))