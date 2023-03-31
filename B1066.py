e_c = 0
o_c = 0
pos_c = 0
neg_c = 0
for i in range(5):
    n = int(input())
    if n % 2 == 0:
        e_c += 1
    else:
        o_c += 1
    if n > 0:
        pos_c += 1
    elif n < 0:
        neg_c += 1

print(e_c," valor(es) par(es)",sep="")
print(o_c," valor(es) impar(es)",sep="")
print(pos_c," valor(es) positivo(s)",sep="")
print(neg_c," valor(es) negativo(s)",sep="")
