import sqlite3

conn = sqlite3.connect('deathrowdb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Sorted''')
cur.execute(''' CREATE TABLE IF NOT EXISTS Sorted (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    word    TEXT UNIQUE,
    count TEXT)''')

print("Sorting the data..........")

cur.execute('SELECT word, count FROM Count')

sorted_dict = dict()
for row in cur:
    try:
        word = cur.fetchone()[0]
        number = cur.fetchone()[1]
    except:
        continue

    sorted_dict[word] = number

new_list = list()
for key,value in sorted_dict.items():
    new_tup = (key, value)
    new_list.append(new_tup)

new_list = sorted(new_list, key=lambda x: int(x[1]), reverse=True)
# print(new_list)

inc = 0
for item in new_list:
    inc = inc + 1
    word = item[0]
    count = item[1]
    print("Word:", word, "**", "Count:", count)
    cur.execute('''INSERT OR IGNORE INTO Sorted (word, count)
                   VALUES ( ?, ? )''', ( word, count) )

    if inc % 100 == 0: conn.commit()

conn.commit()
cur.close()
