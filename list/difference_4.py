l1=[2,4,6,1]
l2=[1,5,2,5,6,7,8]

out=[]
for i in l1+l2:
    if not (i in l1 and i in l2):
    # if (i in l1 or i in l2) and not (i in l1 and i in l2):
        out.append(i)
print('list 1:',l1)
print('list 2:',l2)
print('difference:',out)