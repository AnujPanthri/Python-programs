s='aaaasssssssdaggggdddfdafsafsssd'
out=''
out+=s[0]
for i in range(1,len(s)):
    if out[-1]!=s[i]:
        out+=s[i]
print("Original string:",s)
print("Processed string:",out)

