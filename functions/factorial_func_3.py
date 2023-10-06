def fac(num):
    out=num
    for i in range(2,num):
        out*=i
    return out

print('factorial of 3:',fac(3))
print('factorial of 4:',fac(4))