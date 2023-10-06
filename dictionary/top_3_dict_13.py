d1={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,'item5': 24}
sorted_dict=sorted(list(d1.items()),key=lambda x:x[1],reverse=True)
print(sorted_dict)
print("Top 3 items:")
for item in sorted_dict[:3]:
    print(item[0],item[1])

