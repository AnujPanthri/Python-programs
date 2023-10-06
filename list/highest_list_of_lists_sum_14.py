l1=[[1,2,4],[2,1,6],[2,7,4],[1,4,2]]
highest_sum=[]
for i in l1:
    if sum(i)>sum(highest_sum):
        highest_sum=i

print('list:',l1)
print('list of lists whos sum is highest:',highest_sum)