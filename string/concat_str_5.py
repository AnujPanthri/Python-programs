a="abc"
b="xyz"
result=""

result=b[:2]+a[2:]+' '+a[:2]+b[2:]
print(result)