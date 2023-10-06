s=input()
once=''
repeating=''
for char in s:
    if s.count(char)==1:
        once+=char
    else:
        if char not in repeating:
            repeating+=char

print("character which occured once:",once)
print("character which occured multiple times:",repeating)