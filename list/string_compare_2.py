s1=['abc', 'xyz', 'aba', '1221']
count=0
for s in s1:    
    if s[0]==s[-1] and len(s)>=2:
        count+=1
print(count)