n= int(input())
for x in range(n):
    s=1
    y= int(input())
    for z in range(2,y):
        if y%z==0:
         s=0
    if s==1:
     print("{} eh primo".format(y))
    elif s==0:
     print("{} nao eh primo".format(y))
