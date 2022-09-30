#TODO:
'''
Tìm số nhỏ nhì
'''
list_numbers= [1,3,2,5,4,8,6,7,9]


biggest_number = second_largest_number = list_numbers[0]
for i in range(0, len(list_numbers)):
    if(biggest_number < list_numbers[i]):
        biggest_number = list_numbers[i]
for i in range(0, len(list_numbers)):        
    if(second_largest_number < list_numbers[i] and list_numbers[i] < biggest_number):
        second_largest_number = list_numbers[i]

print("biggest_number: ", biggest_number)
print("second_largest_number: ",second_largest_number)


#hàm có sẵn
#number.sort()
#print (number[-2])


#sắp xếp rồi in số max 2
for i in range(0,len(list_numbers)):
    for j in range(i+1,len(list_numbers)):
        if ( list_numbers [i] < list_numbers [j]):
            temp = list_numbers[i]
            list_numbers[i] = list_numbers [j]
            list_numbers [j] = temp
    
for i in range(0,len(list_numbers)):
    print(list_numbers[i])
print("Số nhỏ nhì la:",list_numbers[1])
