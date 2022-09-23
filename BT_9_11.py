# TODO:
"""
    Viet chuong trinh nhap n so nguyen
    1.in cac so.
    2.tim so lon nhat.
"""
def input_array(lis):
    number = int(input("input number of element:"))
    for i in range(0,number):
        element = int(input("input element: "))
        lis.append(element)    
    return lis


def output_array(lis):
    print(lis)


def search_max(lis):
    max = lis[0]
    for i in range (0, len(lis)):
        if(lis[i] > max):
            max = lis[i]
    return max


if __name__ == "__main__":
    lis = [] 
    input_lis = input_array(lis)
    output_array(input_lis)
    print (f'search max number: {search_max(input_lis)}')
