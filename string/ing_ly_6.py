s=input()
if len(s)>=3:
    if(s[-3:]=="ing"):
        s=s+"ly"
    else:
        s=s+"ing"
print(s)