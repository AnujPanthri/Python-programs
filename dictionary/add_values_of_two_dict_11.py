d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

print('d1:',d1)
print('d1:',d2)
for key in d2:
    if key not in d1.keys():
        d1[key]=0
    d1[key]+=d2[key]
print('final dict:',d1)