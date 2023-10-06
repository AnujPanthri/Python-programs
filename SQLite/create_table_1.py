import sqlite3

con=sqlite3.connect('database.db')
cur=con.cursor()
cur.execute('drop table Hospital')
cur.execute('drop table Doctor')
cur.execute('create table Hospital(Hospital_id char primary key,Hospital_Name char,Bed_Count int);')
cur.execute('create table Doctor(Doctor_id char primary key,Doctor_Name char,Hospital_id char,Joining_Date date,Speciality char,Salary int,Experience int,FOREIGN KEY(Hospital_id) REFERENCES Hospital(Hospital_id));')


