import sqlite3

con=sqlite3.connect('database.db')
cur=con.cursor()

d_id=input("Enter Doctor Id:")
exp=input("Enter Experience(in years):")
cur.execute(f"Update Doctor set Experience=\'{exp}\' where Doctor_id=\'{d_id}\'")
print("Updated Successfully!")
con.commit()