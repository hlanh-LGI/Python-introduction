# TODO:
"""
Xoá phần tử lặp trong list
"""



list_number = [1,2,3,4,2,3]
number_1 = []
for i in list_number:
    if i not in (number_1):
        number_1.append(i)

print (number_1)