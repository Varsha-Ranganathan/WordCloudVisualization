# WordCountVisulatization
Analyzing https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html   
Analyze this website and display a wordcloud using D3 JavaScript library

This is a set of programs that allow you to pull the data about offenders in deathrow
from the above mentioned website and analyse the data for the most used words
by offenders in their last statement.

You should install the SQLite browser to view and modify the databases from:

http://sqlitebrowser.org/

The first step is to access the website and retrieve the name and statement of
each offender. This is done by cleanup.py.

cleanup.py creates a database named 

deathrowdb.sqlite

and creates a table called 'Offenders'

(note that this program deletes all of the tables in the database since
it is not a restartable process)

When the cleanup.py program is run, name and statement of the offenders is pulled from
the website and stored in the 'Offenders' table.

cleanup.py is not a restartable process, The table is deleted and created every time and
hence data gathering connot be done at various times. (It must be done in a single shot)

The second step is running wordcount.py

this creates a table in deathrowdb.sqlite named 'Count'

The statement from 'Offenders' table is taken and the frequency of everyword is counted.
The word and corresponding count is stored back into the 'Count' table.

The third step is running sortcount.py

this creates a table in deathrowdb.sqlite named 'Sorted'

the word and count from 'Count' table is pulled out and the count is arranged in
descending order, ranging from maximum used words to minimum used words.

The fourth step is running wordjs.py

this writes the gword.js file which is further used for visualization.

wordjs.py enables to display upto first 100 words from 'Sorted' table.

wordjs.py takes the data from 'Sorted' table and assigns font size according to
their usage(i.e count) for each word, to be displayed in the wordcloud.

output is written to gword.js and the output can be viewed by opening gword.htm

gword.js, d3.layout.cloud and d3.v2 are JavaSript files provided in the online class - Coursera,
'Python for Everybody' by Dr.Chuck and is used to display the word cloud.

Summary:

None of these python programs are restartable, it has to be strated from the scratch
everytime around.

1. cleanup.py to pull data from website
2. wordcount.py to count the usage of words from the statements
3. sortcount.py to arrabge the data from wordcount.py in descending order
4. wordjs.py to write javascript file for the word cloud
5. gword.js is the JavaScript file written by wordjs.py
6. output can be viewed in gword.htm

(To be able to view the word cloud, sqlite must be installed and all these scripts must be executed in order)
(Attached a non-dynamic pie-chart of a smaller version of this project for reference)
--------
R.Varsha 29 July 2020 19:16 India

                               





