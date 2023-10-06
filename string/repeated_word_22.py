s=input()
all_words=s.split()

for i in range(len(all_words)):
    if all_words.count(all_words[i])>1:
        print("first repeated word:",all_words[i])
        break
