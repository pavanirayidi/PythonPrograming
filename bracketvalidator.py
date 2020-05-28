''' Given a string of brackets (, ), {, }, [, ], find the position in the string where the orders of brackets breaks.
I/p: ())
O/p: 3
 
I/p: (){[]}(
O/p: 8  '''

def validator(s):
    stack=[]
    count=0
    for b in s:
        if b=='(' or b=='[' or b=='{' :
            stack.append(b)
            count+=1
            continue
        if len(stack)==0:
            return count+1
        x=stack.pop()
        if b==')' and x=='(':
            count+=1
        elif b==']' and x=='[':
            count+=1
        elif b=='}' and x=='{':
            count+=1
        else:
            return count+1
    if len(stack)==0:
        return 0
    else:
        return count+1
s=input()
print(validator(s))
                
