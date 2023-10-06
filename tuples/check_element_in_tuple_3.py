t1=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange','Yellow', 'Lime'))
val=input('enter element to search:')
print()
for t in t1:
    if t.count(val)>0:
        print(val,' is present is tuple of tuples')
        break
else:
    print(val,' is not present is tuple of tuples')