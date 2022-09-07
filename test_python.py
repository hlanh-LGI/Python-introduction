number =int(input('input of number:'))
"""erro: > not support str and int"""   
print(number) 
sum=0     
while (number > 10):
    sum=sum+number%10
    number=int(number/10)
    sum=sum+number
print(sum)

