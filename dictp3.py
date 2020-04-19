"""python function to create and return a new dictionary from the given dictionary(item:price).
Given the following input, create a new dictionary with elements having price more than 200.

prices = {'ACME': 45.23,'AAPL': 612.78, 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75} """

def create_new_dictionary(prices):

    #start writing your code here

    new_dict = {}

    for k,g in prices.items():

        if g>200:

            new_dict[k]=g

    return new_dict



# Let prices dictionary for input be { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}

prices = eval(input())

print(create_new_dictionary(prices))
