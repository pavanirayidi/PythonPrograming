'''INPUT :coronavirus
          3
           abcde
           crnas
           onarous
OUTPUT :
          NEGATIVE
          POSITIVE
          NEGATIVE'''

str2=input()
n=int(input())
c=0
def check(str1,str2):
        if len(str1)==0:
            print("POSITIVE")
        i=j=0
        while i<len(str1)and j<len(str2):
            a=str1[i]
            b=str2[j]
            if a==b:
                i+=1 
            if len(str1)==i:
                print("POSITIVE")
                break
            j+=1
        else:
                print("NEGATIVE")
while n>c:
        c+=1
        str1=input()
        check(str1,str2)
