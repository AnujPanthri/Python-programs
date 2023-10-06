l1=[1,2,4,5,1,2,423]
print('original list:',l1)
k=int(input("Enter K:"))-1
print()
l2=l1[:k]+l1[k+1:]
print('kth element removed:',l2)