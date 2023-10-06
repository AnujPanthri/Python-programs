s=input()
all_words=s.split()
words=list(set(all_words))
count=[]
for word in words:
    count.append(all_words.count(word))
# print(words)
# print(count)
for i in range(len(count)):#bubble sort
    for j in range(len(count)-i-1):
        if count[j]<count[j+1]:
            count[j]=count[j]+count[j+1]
            count[j+1]=count[j]-count[j+1]
            count[j]=count[j]-count[j+1]
            temp=words[j]
            words[j]=words[j+1]
            words[j+1]=temp

# print(words)
# print(count)
print("second most used word is:",words[1])
