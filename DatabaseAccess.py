import sqlite3

conn = sqlite3.connect('/home/mone2/openbsc-0.14.0/openbsc/src/hlr.sqlite3')
c = conn.cursor()
c.execute('SELECT * FROM Subscriber;')
temp = c.fetchone()

print(temp)