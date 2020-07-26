''' Given two strings, determine if they share a common substring. A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.

Function Description

Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.

twoStrings has the following parameter(s):

s1, s2: two strings to analyze .

Sample Input                          Sample Output
2                                       YES
hello                                   NO
world
hi
world'''


a = int(input())
for i in range(a):
    i = str(input())
    j = str(input())
    setx = set([a for a in i])
    sety = set([y for y in j])
    if setx.intersection(sety) == set():
        print("NO")
    else:
        print("YES")
