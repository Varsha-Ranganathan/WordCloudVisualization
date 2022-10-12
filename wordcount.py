import sqlite3
import string
import time

conn = sqlite3.connect('deathrowdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Count')

cur.execute('''CREATE TABLE IF NOT EXISTS Count (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    word    TEXT UNIQUE,
    count TEXT )''')

cur.execute('SELECT statement FROM Offenders')

count = 0
word_dict = dict()
for row in cur:
    try:
        statement = cur.fetchone()[0]
        count = count + 1
    except:
        continue
    # print(statement)
    # print('====================================================================')

    # split the stement and clean up for punctuations
    words = statement.split()
    for word in words:
        word = word.translate(word.maketrans("", "", string.punctuation))
        word = word.strip()
        word = word.lower()
        if len(word) < 2: continue # words like a, I will also be ignored
        word_dict[word] = word_dict.get(word, 0) + 1

# print(len(word_dict))

cur.execute('SELECT word, count FROM Count')

for word, count in word_dict.items():
    cur.execute('''INSERT OR IGNORE INTO Count (word, count)
    VALUES ( ?, ? )''', ( word, count ) )
    print("Word:", word, "**   Count:", count )

    if count % 100 == 0:
        print('Updating the database.............')
        conn.commit()
        time.sleep(2)

conn.commit()
cur.close()
