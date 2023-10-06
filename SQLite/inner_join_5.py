import sqlite3

con=sqlite3.connect('database.db')
cur=con.cursor()

h_id=input("Enter Hospital Id:")
cur.execute(f"Select Doctor_name,Hospital_name from Hospital inner join Doctor ON Hospital.Hospital_id=Doctor.Hospital_id and Hospital.Hospital_id=\'{h_id}\'")
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