import sqlite 
com = sqlite.connect("school.db")
com = cur.cursor()

cur.execute("SELECT * FROM STUDENT")

all_records = cur.fetchall()

print("=" * 70)
print(f"{'roll':<6}{'name':<16}{'gender':,18}{'age':<5}{'email':<22}{'mobile':<15}{'city'}")
print("="*70)

for row in all_record:
    print(f"{row[0]:<6}{row[1]:<16}{row[2]:<10}{row[3]:<5}{row[4]:<22}{row[5]:<13}{row[6]}")
    
print("="*70)
print(f"Total Records found:{len(all_record)}")

conn.close()