l1=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l2=[l1[0]]
for i in l1[1:]:
    if i!=l2[-1]:
        l2.append(i)

print("original List:",l1)
print("Final List:",l2)
