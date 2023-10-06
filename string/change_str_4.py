s=input()
result=''
result+=s[0]
for i in range(1,len(s)):
    if s[0]==s[i]:
        result+="$"
    else:
        result+=s[i]
print(result)