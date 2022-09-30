#TODO:
'''
Write a Python program to find common items from two lists.
'''

list_a = [1,24,2,5,7,4]
list_b = [4,5,7,10,9,8]

number = 0
for i in range(0,len(list_a)):
    for j in range(0,len(list_b)):
        if(list_a[i]== list_b[j]):
            number = number + 1
print(number)