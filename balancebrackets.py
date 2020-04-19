'''Write a python function which accepts a string containing a pattern of brackets and returns true if the pattern of brackets is correct. Otherwise it returns false.

The string of brackets is correct if it satisfies the following conditions:
1. Number of opening and closing brackets are equal.
2. Pattern should not start with closing bracket and end with opening bracket.'''

#PF-Prac-2
def bracket_pattern(input_str):
    #Remove pass and write your code here
    if input_str.startswith(')')or input_str.endswith('('):
        return False
    else:
        c=0
        for p in input_str:
            if p=='(':
                c+=1
            else:
                c-=1
        result=True if c==0 else False
    return result

    
input_str="()((())())"
print(bracket_pattern(input_str))
