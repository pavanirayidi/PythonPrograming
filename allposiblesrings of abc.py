p = permutations(a,1)
for i in range (len(a)):
    for j in p:  
        b="".join(j)
        print(b)
OP:
a
b
c
ab
ac
ba
bc
ca
cb
abc
acb
bac
bca
cab
cba
