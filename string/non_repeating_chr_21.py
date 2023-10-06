s=input()
for i in range(len(s)):
    if s.count(s[i])==1:
        print("first non-repeating character:",s[i])
        break
