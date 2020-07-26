'''  You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, given the string , remove an  at positions  and  to make  in  deletions.

Function Description

Complete the alternatingCharacters function in the editor below. It must return an integer representing the minimum number of deletions to make the alternating string.

alternatingCharacters has the following parameter(s):

s: a string

Sample Input                              Sample Output

5                                           
AAAA                                        3
BBBBB                                       4
ABABABAB                                    0
BABABA                                      0
AAABBB                                      4           '''


n=int(input())
for j in range(n):
    c=0
    s=input()
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            c+=1
    print(c)
