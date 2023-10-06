s=input("enter words with space in between:")
words=s.split()
longest_len=0
for word in words:
    if len(word)>longest_len:
        longest_len=len(word)
print("the length of the longest word is:",longest_len)