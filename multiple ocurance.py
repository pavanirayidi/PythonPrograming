# Write your code here
N=int(input())
while(N):
    N1=int(input())
    sum=0
    l = list(map(int,input().split()))
    l1=set(l)
    for i in l1:
        s=l.index(i)
        r=len(l)-1-l[::-1].index(i)
        sum=sum+r-s
    print(sum)
    N=N-1


