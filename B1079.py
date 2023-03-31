n = int(input())
for x in range(n):
    x1, x2, x3 = [float(x) for x in input().split()]
    w_avg = (x1 * 2 + x2 * 3 + x3 * 5) / (2 + 3 + 5)
    print("%.1f" % w_avg)