a=input()
b=[]
from itertools import permutations
for i in range (len(a)+1):
    p = permutations(a,i)
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
