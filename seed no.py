
#PF-Prac-7
def seed_no(number,ref_no):
    #start writing your code here
    p=1
    for i in str(number):
        p=p*int(i)
    return p*number==ref_no
number=123
ref_no=738
print(seed_no(number,ref_no))
