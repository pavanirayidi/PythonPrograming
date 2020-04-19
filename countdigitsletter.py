Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.

It should return a list in which the first value should be letter count and second value should be digit count. Ignore the spaces or any other special character in the sentence.
Sample Input
Expected Output
Infosys 123         ABCEFG
[7,3]               [6,0]


#PF-Prac-5
def count_digits_letters(sentence):
    #start writing your code here
    c=c1=0
    result_list=[]
    for i in sentence:
        if i.isalpha():
            c=c+1
        if i.isdigit():
            c1=c1+1
    result_list.append(c)
    result_list.append(c1)
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
