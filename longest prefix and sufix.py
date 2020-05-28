'''Given a string, find the longest length of a prefix which is also a suffix.
https://www.geeksforgeeks.org/longest-prefix-also-suffix/'''


s=input()
for i in range(len(s)//2,0,-1):
    p=s[0:i]
    su=s[len(s)-i :len(s)]
    if p==su:
        print(len(p))
        break
    else:
        print(False)
        
