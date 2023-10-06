l1=["ss","tyu","ss","yu","tyu"]
l2=[]

l2.append(l1[0])
for i in l1[1:]:
    if i not in l2:
        l2.append(i)
print(l2)