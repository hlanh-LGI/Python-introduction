# TODO: 
"""
1. 
2.
3.

"""

# DEBUG: 
"""error: > not support str and int"""   


# print(f'number: {number}')  

# name = 'long'
# print('number: {}, name: {}'.format(number, name))

def sum_number(number):
    sum = 0 
    while (number > 10): 
        sum=sum+number%10
        number=int(number/10)
    sum=sum+number
    return sum

if __name__ == "__main__":
    number =int(input('Input number: '))
    print("number:",number) 
    print(sum_number(number))
