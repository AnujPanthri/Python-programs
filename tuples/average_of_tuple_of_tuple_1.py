t1=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3,4))
avg_list=[]
for t in t1:
    avg_list.append(sum(t)/len(t))
print(t1)
print(avg_list)