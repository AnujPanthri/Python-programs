def count_upper_lower(str1):
    lower=0
    upper=0
    for ch in str1:    
        if ch.islower():
            lower+=1
        elif ch.isupper():
            upper+=1
    print('No. of Upper case characters :',upper)
    print('No. of Lower case Characters :',lower)

s1=input("Enter String:")
count_upper_lower(s1)