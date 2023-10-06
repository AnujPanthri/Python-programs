import sqlite3

con=sqlite3.connect('database.db')
cur=con.cursor()
ch=input("Enter h or d for hospital or doctor:")
if ch=='h':
    h_id=input("Enter Hospital Id:")
    cur.execute(f"Select * from Hospital where Hospital_id=\'{h_id}\'")
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
elif ch=='d':
    d_id=input("Enter Doctor Id:")
    cur.execute(f"Select * from Doctor where Doctor_id=\'{d_id}\'")
    data=cur.fetchall()
    names = [description[0] for description in cur.description]
    for name in names:
        print("\t",name, end='',sep='')
    print()
    for i,rows in enumerate(data):
        print((i+1),'. ',sep='',end='')
        # print("\t",end='')
        for j in range(len(rows)):
            print('\t\t',rows[j],end=' ')