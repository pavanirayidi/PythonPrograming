s=input()
p=""
o=""
for i in range(len(s)):
    if s[i].isalpha():
        p+=s[i]
b=p[::-1]
c=0
for i in range(len(s)):
    if s[i].isalpha():
        o+=b[c]
        c+=1
    else:
        o+=s[i]
print(o)
