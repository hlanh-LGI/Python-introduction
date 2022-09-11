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

if __name__ == "__main__":
    lis = []
    print(input_array(lis))