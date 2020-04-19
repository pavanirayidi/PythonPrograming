
#PF-Tryout
def diagonal_stars(number):
   #start writing your code here
   for i in range(number):
        for j in range(i):
            print('.',end="")
        for j in range(i+1):
            if i==j:
                print('*',end="")
        print('\n')

number=6    
diagonal_stars(number)
