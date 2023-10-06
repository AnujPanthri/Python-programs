# s=" red, white, black, red, green, black"
s=input()
words=s.split(',')
words=sorted(set(words))
print(",".join(words))