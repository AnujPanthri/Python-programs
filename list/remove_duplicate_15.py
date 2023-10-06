l1=[[10, 20], [40], [30, 56, 25], [10, 20], [33],[40]]
l2=[]

l2.append(l1[0])
for i in l1[1:]:
    if i not in l2:
        l2.append(i)
print(l2)