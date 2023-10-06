s=input()
n=3

new_s=''
for char in s:
    new_s+=chr(ord(char)-n)
print(new_s)