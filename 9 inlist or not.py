'''Given a list of numbers, write a python function which returns true if one of the first 4 elements in the list is 9. Otherwise it should return false.
The length of the list can be less than 4 also.
[1, 2, 9, 3, 4]
True
[1, 2, 9]
True
[1, 2,3,4]
False'''

#PF-Prac-4
def find_nine(nums):
    #Remove pass and write your code here
    s=nums[:5]
    if 9 in s:
        return True
    else:
        return False
nums=[12, 3, 4, 5, 9]
print(find_nine(nums))
