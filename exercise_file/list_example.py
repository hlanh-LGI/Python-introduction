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


if __name__=="__main__":
    lis=[1, 2, 3, 4]

    # check list
    check_list(lis)

    # find maximum number
    print(f'Max number: {find_max_number(lis)}')
