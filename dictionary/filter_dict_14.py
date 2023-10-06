d1={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'PierreCox': 190}
print('d1:',d1,'\n')
val=list(filter(lambda x:d1[x]>170,d1))
print('Marks greater than 170:')
for v in val:
    print(v,d1[v],', ',end='')
