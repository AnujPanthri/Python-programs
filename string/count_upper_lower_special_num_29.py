s="23efasdf77E$^"
u_c=0
l_c=0
n_c=0
s_c=0
for char in s:
    if char.isupper():
        u_c+=1
    elif char.islower():
        l_c+=1
    elif char.isnumeric():
        n_c+=1
    else:
        s_c+=1
print("Number of upper case characters in string:",u_c)
print("Number of lower case characters in string:",l_c)
print("Number of special characters in string:",s_c)
print("Number of numeric values in string:",n_c)

