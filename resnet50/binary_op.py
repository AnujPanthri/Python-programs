
def Binary_sub(a,b):
    while(b!=0):
        borrow=~a&b
        a=a^b
        b=borrow<<1
    return a
    
def Binary_add(a,b):
    while(b!=0):
        carry=a&b
        a=a^b
        b=carry<<1
    return a

print(Binary_add(2,4))
print(Binary_add(5,26))

print(~2)
# print(Binary_sub(2,4))
# print(Binary_sub(5,26))