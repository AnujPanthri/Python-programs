import sqlite3

con=sqlite3.connect('database.db')
cur=con.cursor()


min_sal=input("Enter minimum salary:")
spec=input("Enter Speciality:")
cur.execute(f"Select Doctor_name from Doctor where salary>\'{min_sal}\' and Speciality=\'{spec}\'")
# cur.execute("Select * from Hospital")
data=cur.fetchall()
names = [description[0] for description in cur.description]
for name in names:
    print("\t",name, end='',sep='')
print()
for i,rows in enumerate(data):
    print((i+1),'. ',sep='',end='')
    print("\t",end='')
    for j in range(len(rows)):
        print('\t',rows[j],end=' ')
    print()