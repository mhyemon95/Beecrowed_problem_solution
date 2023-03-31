def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
for x in range(n):
    print(fib(x),end=" ")