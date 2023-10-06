s=input()
result=""
if(len(s)>=2):
    result+=s[:2]
    result+=s[-2:]
    print(result)
else:
    print("Empty String")
