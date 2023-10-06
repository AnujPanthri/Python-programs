a="asdfe"
b="qwasdes"
both=a+b
bothchars=set(both)
c=""

# chardict={char:0 for char in bothchars}
# for char in both:
#     chardict[char]+=1
# for char in chardict:
#     if chardict[char]==1:
#         print(char)

for char in bothchars:
    if both.count(char)==1:
        c+=char
print(c)


# common=False
# a_copy=a
# b_copy=b
# for i in range(len(a)):
#     common=False
#     for j in range(len(b_copy)):
#         if a[i]==b_copy[j]:
#             common=True
#             print("common_chars:",a[i])
#             b_copy=b_copy[0:j]+b_copy[j+1:]
#             print(b_copy)
#     if common==True:
#         a_copy=a_copy[0:i]+a_copy[i+1:]
# print("a:",a)        
# print("a:",a_copy)        
# print("b:",b)        
# print("b:",b_copy)       
# print("uncommon character from string a and b are:",c)
        