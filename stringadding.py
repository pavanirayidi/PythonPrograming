'''Write a python function to add 'ing' at the end of a given string and return the new string. 
If the given string already ends with 'ing' then add 'ly'.
If the length of the given string is less than 3, leave it unchanged.'''


#PF-Prac-1
def add_string(str1):
  #start writing your code here
    if str1.endswith("ing"):
      return str1+'ly'
    elif len(str1)<3:
        return str1
    else:
        return str1+'ing'
str1="com"
print(add_string(str1))
