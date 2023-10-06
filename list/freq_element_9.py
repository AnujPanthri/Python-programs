l1=[1,2,7,7,5,2,5,6,7,8]
out=[]

for i in l1:
    if out.count([i,l1.count(i)])==0:
        out.append([i,l1.count(i)])
print('list:',l1,'\n\n')
print('frequency of the elements:')
for item in out:
    print(item[0],":",item[1])