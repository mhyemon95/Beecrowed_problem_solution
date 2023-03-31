x=int(input())
y=int(input())
sum=0
for n in range(y+1,x):
    if (n%2!=0):
        sum+=n
print(sum)