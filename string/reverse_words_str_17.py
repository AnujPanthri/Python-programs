s='hello world'
words=s.split()
for i in range(len(words)):
    words[i]=words[i][::-1]
final_str=" ".join(words)
print(final_str)
