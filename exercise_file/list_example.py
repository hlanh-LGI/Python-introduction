def check_list(lis: list):
    """
        check list
    """
    if len(lis)==0:
        print ("Empty list !!!")
    else:
        print("List have the element !!!")

def find_max_number(lis: list):
    """
        Find maximum number of this list
    """
    biggest_number = lis[0]
    for element in lis:
        if biggest_number < element:
            biggest_number = element
    return biggest_number

def find_max_second_number(lis: list):
    """
    find second largest number of this list
    """
    second_largest_number = lis[0]
    for i in lis:        
        if second_largest_number < i and i < find_max_number(lis) :
            second_largest_number = i
    return second_largest_number

def sum_list(lis: list):
    """
    find sum of list

    """
    sum=0
    for element in lis:
        sum = sum + element
    return sum

def find_common_items(lis: list):
    number = 0
    for i in range(0,len(lis)):
        for j in range(0,len(lis_1)):
            if(lis[i]== lis_1[j]):
                number = number + 1
    return number

def insert_element(lis: list):
    list1 = lis[0 : 1]
    list3 = lis[1 :  ]
    list2= [5]
    return list1 + list2 + list3

def delete_element(lis: list):
    for i in lis:
        if i not in (lis_2):
            lis_2.append(i)
    return  lis_2
if __name__=="__main__":
    lis=[1, 2, 3, 4,123,5,2,78]
    lis_1 = [1,5,3,4]
    lis_2 = []
    # check list
    check_list(lis)

    # find maximum number
    print(f'Max number: {find_max_number(lis)}')

    #find second largest number
    print(f'Max_second number: {find_max_second_number(lis)}')

    #find sum of list
    print(f'sum number of list : {sum_list(lis)}')

    #find common items from two lists.
    print(f'find_common_items : {find_common_items(lis)}')

    #insert_element
    print(f'insert_element : {insert_element(lis)}')

    #delete_element
    print(f'delete_element : {delete_element(lis)}')