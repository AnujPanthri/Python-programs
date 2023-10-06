s=input()
count=0
for i in range(4):
    if s[i].isupper():
        count+=1
if count>=2:
    s=s.upper()
print(s)
