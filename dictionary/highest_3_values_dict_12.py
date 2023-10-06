d1={'a':'anger','v':'van','s':'sleep','an':'abroad','l':'life','b':'building'}

sorted_values=sorted(list(d1.values()),reverse=True)
print('Highest 3 values of dictionary:')
for i in range(3):
    print(i+1,'.',sorted_values[i])