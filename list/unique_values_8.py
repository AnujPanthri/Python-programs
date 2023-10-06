l1=[1,2,7,7,5,2,5,6,7,8]
out=[]
for i in range(len(l1)):
    repeat=False
    for j in range(len(l1)):
        if l1[i]==l1[j] and i!=j:
            repeat=True
            break
    if not repeat:
        out.append(l1[i])
print('list:',l1)
print("unique elements:",out)
