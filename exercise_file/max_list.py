#TODO:
"""
tim so lon nhat
"""

list_number = [1,2,3,4,4,5,6,6]
biggest_number = list_number[0]
for elemnet in range(0, len(list_number)):
    if (biggest_number < list_number[elemnet]) :
        biggest_number = list_number[elemnet]

print(biggest_number)

print (max(list_number))