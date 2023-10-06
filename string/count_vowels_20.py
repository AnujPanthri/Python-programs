s="asdee34dfgdfg df00"
vowels=['a',0,'e',0,'i',0,'o',0,'u',0]
for i in range(0,len(vowels),2):
    count=s.count(vowels[i])
    vowels[i+1]=count

for i in range(0,len(vowels),2):
    if vowels[i+1]>0:
        print(vowels[i],":",vowels[i+1])
