'''Write a python function that accepts a list of words and returns the list of integers representing the length of the corresponding words.

Sample Input	Expected Output
[cat, Come]	[3,4]'''

#PF-Prac-25
def list_of_count(word_list):
    #start writing your code here
    count_list=[]
    for i in word_list:
        count_list.append(len(i))
    
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))
