import sqlite3

conn = sqlite3.connect('deathrowdb.sqlite')
cur = conn.cursor()

cur.execute('SELECT min(id), word, count FROM Sorted')
highest = cur.fetchone()[2]
highest = int(highest)

cur.execute('SELECT max(id), word, count FROM Sorted')
lowest = cur.fetchone()[2]
lowest = int(lowest)

# print(highest, lowest)

cur.execute('SELECT word, count FROM Sorted')

inc = 0
word_dict = dict()
x = list()
for row in cur:
    word = row[0]
    count = row[1]
    inc = inc + 1
    x.append(word)
    # print(word, count)
    word_dict[word] = count
# print(x)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('gword.js','w')
fhand.write("gword = [")
first = True
for k in x[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = word_dict[k]
    size = int(size)
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+ k +"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

print("Output written to gword.js")
print("Open gword.htm in a browser to see the vizualization")
