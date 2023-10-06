t1 = (('a', 23),('b', 37),('c', 11), ('d',29))
print('Original t1:',t1)

print('Sorted t1:',tuple(sorted(t1,key=lambda x:x[1])))