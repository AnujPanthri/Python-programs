def perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return True
    else:
        return False
n=int(input('Enter a Number:'))

print(n,'is perfect number:',perfect_number(n))