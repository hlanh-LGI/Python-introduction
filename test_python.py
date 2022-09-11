# TODO: 
"""
1. Enter int n.Sum of number in n.
2. Enter int n.reverse number printing(in so dao nguoc).
3. enter integer n. Checks if n is prime or not.(kiem tra n co phai la so nguyen to hay khong)

"""

# DEBUG: 
"""error: > not support str and int"""   


# print(f'number: {number}')  

# name = 'long'
# print('number: {}, name: {}'.format(number, name))
'''1.Enter an int N.Sum of number in n.'''
def sum_number(number):
    sum = 0 
    while (number > 10): 
        sum=sum+number%10
        number=int(number/10)
    return sum

if __name__ == "__main__":
    number =int(input('Input number: '))
    print("number:",number) 
    print(sum_number(number))
