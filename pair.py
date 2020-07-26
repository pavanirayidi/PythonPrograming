'''     You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.

For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: , , and .

Sample Input                        Sample Output

5 2                                   3
1 5 3 4 2  

Explanation

There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1] .'''



n,k=map(int,input().split(' '))
count=0
list1 = list(map(int, input().rstrip().split()))
#list1=list(map(int,[input() for i in range(n)]))
for i in range(n):
    for j in range(n):
        if list1[i]-list1[j]== k:
            count+=1
print(count)
