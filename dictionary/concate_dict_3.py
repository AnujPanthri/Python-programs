d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50,6:60}

print('d1:',d1)
print('d2:',d2)
print('d3:',d3)

d1.update(d2)
d1.update(d3)
print('\nall concatenated:',d1)