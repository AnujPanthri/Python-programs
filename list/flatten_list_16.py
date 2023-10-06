l1=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100,110, 120]]
l2=[]
for i in l1:
    if type(i)==list:
        l2.extend(i)
    else:
        l2.append(i)
print(l2)