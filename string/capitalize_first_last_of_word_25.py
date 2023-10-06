s=input()
words=s.split()
result=''
for i in range(len(words)):
    result+=words[i][0].upper()+words[i][1:len(words[i])-1]
    if len(words[i])!=1:
        result+=words[i][-1].upper()
    if i!=len(words)-1:
        result+=' '
print(result)