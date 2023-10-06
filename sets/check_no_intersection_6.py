s1={2,5,3,4,5,17,3}
s2={1,6,7,8,9}
#s2={1,3,5,2,6}

print('s1:',s1)
print('s2:',s2)

if len(s1.intersection(s2))==0:
    print("no common elements found")
else:
    print("common elements found")
