
#PF-Prac-23
def divisible_by_sum(number):
    #start writing your code here
    s=0
    for n in str(number):
        s=s+int(n)
    return number%s==0
    

    
number=66
print(divisible_by_sum(number))
