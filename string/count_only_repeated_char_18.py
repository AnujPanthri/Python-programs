s="thequickbrownfoxjumpsoverthelazydog"
allchars=set(s)
print("Character Frequency:")
for char in allchars:
    if (s.count(char)>1):
        print(char,":",s.count(char))