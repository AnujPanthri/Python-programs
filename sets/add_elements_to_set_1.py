s1=set()
# print(type(s1))
n=int(input('number of elements to add to set:'))
for i in range(n):
    s1.add(int(input('enter elements:')))
for i in s1:
    print(i,end=',')