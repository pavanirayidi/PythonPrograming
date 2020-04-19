Write a python function which accepts a list of numbers and returns true, if 1, 2, 3 appears in sequence in the list.

Otherwise, it should return false.
Sample Input  : [1, 1, 2, 3, 1],    [1, 1, 2, 4, 3]
Expected Output :True ,             False


#PF-Prac-6
def list123(nums):
    #start writing your code here
    c=0
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            c=c+1
    if c>0:
        return True
    else:
        return False
nums=[1,2,3,4,5]
print(list123(nums))
