#PF-Prac-24
def find_gcd(num1,num2):
    #start writing your code here
    small=gcd=0 
    if num1<num2:
        small=num1
    else:
        small=num2
    for i in range(1,small+1):
        if num1%i==0 and num2%i==0:
            gcd=i
    return gcd
    

num1=800
num2=2800
print(find_gcd(num1,num2))
