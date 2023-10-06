import sqlite3
from datetime import date

con=sqlite3.connect("database.db")
cur=con.cursor()
cur.execute("PRAGMA foreign_keys = 1")
ch=input('Enter h or d for inserting hospital or doctor details:')

if ch.lower()=='h':
    h_id=input("Hospital Id:")
    h_name=input("Hospital Name:")
    b_count=input("Bed Count:")
    con.execute(f'insert into Hospital values(\'{h_id}\',\'{h_name}\',\'{b_count}\')')

elif ch.lower()=='d':
    d_id=input('Doctor Id:')
    d_name=input('Doctor Name:')
    h_id=input('Hospital Id:')
    j_date=input('Joining Date(DD-MM-YYYY):').split('-')
    j_date=list(map(int,j_date))
    j_date=date(j_date[-1],j_date[-2],j_date[-3])
    # print(j_date)
    spec=input('Speciality:')
    salary=input('Salary:')
    experience=input('Experience(years):')

    con.execute(f'insert into Doctor values(\'{d_id}\',\'{d_name}\',\'{h_id}\',\'{j_date}\',\'{spec}\',\'{salary}\',\'{experience}\')')


con.commit()