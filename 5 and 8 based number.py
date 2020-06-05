'''Input integers are separated by comma(,).Form num1 by adding all the numbers except which are present in between 5 and 8.And num2 by concating numbers from 5 to 8.Then display the sum of num1 and num2. 
Sample Input 0
3,2,6,5,1,4,8,9
Sample Output 0
5168'''


s=input().split(",")
num1=0
s1=s[s.index('5'):s.index('8')+1]
num2="".join(s1)
for i in range(len(s)):
    if s[i] not in s1:
        num1+=int(s[i])
print(num1+int(num2))
