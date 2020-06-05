'''Every string is associated with the number separated by colon(:).Task is to rotate the string based on the number. If the sum of square of digits is even then rotate the string right by 1 position else rotate the string left by 2 position.

Sample Input 0
rhdt:246,ghftd:1246
Sample Output 0
trhd ftdgh'''

s=input().split(",")
for i in s:
    k=0
    s1=i.split(":")
    str1=s1[0]
    num=s1[1]
    for j in range(len(str(num))):
        k+=int(num[j])*int(num[j])
    if k%2==0:
            print(str1[-1]+str1[0:-1],end=" ")
    else:
            
            print(str1[2::]+str1[0:2],end=" ")

