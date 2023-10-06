s1={1,3,5,2,6}
s2={2,5,3,4,5,17,3}
print("set 1:",s1)
print("set 2:",s2)
print("Union:",s1.union(s2))
print("Intersection:",s1.intersection(s2))
print('difference(set1 and set2):',s1.difference(s2))
print('difference(set2 and set1):',s2.difference(s1))
print('Symeterical difference:',s1.symmetric_difference(s2))