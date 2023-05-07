X,Y = map(int,input().split())
i = {1:4.0,2:4.5,3:5.0,4:2.0,5:1.5}
X = float(i[X])*Y
print(f"Total: R$ {X:.2f}")