d1={'1':10,'2':20,'4':40,'5':50}

k=input("enter key to search for:")
if list(d1.keys()).count(k)==0:
    print('\"',k,"\" key not found in dictionary")
else:
    print('\"',k,"\" key found in dictionary")