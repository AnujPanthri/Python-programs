d1={'a':'anger','v':'van','s':'sleep','l':'life','b':'building'}
print(d1)
print("Sorted in accending order:",sorted(d1.items(),key=(lambda x:x[1])  ) )
print("Sorted in decending order:",sorted(d1.items(),key=(lambda x:x[1])  ,reverse=True) )
