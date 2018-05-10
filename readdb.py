import sqlite3

conn = sqlite3.connect('resultsdb.sqlite')
c = conn.cursor()
for row in c.execute('SELECT * FROM Results ORDER BY burglaries'):
    print(u'{1} burglaries have happened at {0}'.format(row[0], row[1]))
