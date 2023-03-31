def perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


y = int(input())
for i in range(y):
    n = int(input())
    result = "eh perfeito" if perfect(n) else "nao eh perfeito"
    print(f"{n} {result}")

