while True:
    x = int(input())
    if x == 0:
        break
    if x % 2 == 0:
        print(sum(range(x, x+10, 2)))
    else:
        print(sum(range(x+1, x+11, 2)))
