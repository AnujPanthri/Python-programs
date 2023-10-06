
def pangram(str1):
    str1=str1.lower()
    allchars='abcdefghijklmnopqrstuvwxyz'
    pangram=True
    for char in allchars:
        if char not in str1:
            pangram=False
            break
    return pangram
        
s=input("Enter String:")
print(s,'is pangram:',pangram(s))