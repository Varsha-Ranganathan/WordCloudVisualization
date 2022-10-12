import urllib.request
from bs4 import BeautifulSoup
import re
import sqlite3
import string
import time

conn = sqlite3.connect('deathrowdb.sqlite')
cur = conn.cursor()

# cur.execute('''DROP TABLE IF EXISTS Offenders''')
# cur.execute('''DROP TABLE IF EXISTS Sorted''')
# cur.execute('DROP TABLE IF EXISTS Count')

cur.execute(''' CREATE TABLE IF NOT EXISTS Offenders (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE,
    statement TEXT)''')

html = urllib.request.urlopen("https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html").read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

count = 0
number = 0
for tag in tags:
    part = tag.get('href', None)
    if part is None: continue

    url = "https://www.tdcj.texas.gov/death_row/" + part
    last = re.findall('(https://www\.tdcj\.texas\.gov/death_row/dr_info/[a-z]+last\.html)', url)
    if not last: continue
    # count = count + 1

    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    para = soup('p')

    # pull out the first item from the list
    item = para[0]

    # skip through the <p> tags to get to the name of the offenders
    ignore = item.find_next('p')
    for i in range(2):
        ignore = ignore.find_next('p')
    try:
        name = ignore.text
        if 'Offender:' in name:
            ignore = ignore.find_next('p')
            try:
                name = ignore.text
            except:
                print("***** Unable to retrieve name *****")
                continue
    except:
        print("***** Unable to retrieve name *****")
        continue
    try:
        pos = name.find("#")
        name = name[:pos]
    except:
        pass
    try:
        pos = name.find("TDCJ")
        name = name[:pos]
    except:
        pass
    name = name.translate(name.maketrans("", "", string.punctuation))
    name = name.strip()

    # skip through the <p> tags to get to the statement of the offenders
    ignore = item.find_next('p')
    for i in range(4):
        ignore = ignore.find_next('p')
    try:
        statement = ignore.text
        if 'Last Statement:' in statement:
            ignore = ignore.find_next('p')
            try:
                statement = ignore.text
            except:
                print("***** Unable to retrieve statement *****")
                continue
    except:
        print("***** Unable to retrieve statement *****")
        continue

    count = count + 1
    print('=========================' + str(count) + '=============================')
    print('Name:',name)
    print('Statement:', statement)

    cur.execute('''INSERT OR IGNORE INTO Offenders (name, statement)
        VALUES ( ?, ? )''', ( name, statement) )

    if count % 25 == 0:
        time.sleep(5)
        print('Updating the database............')
        conn.commit()

conn.commit()
cur.close()
