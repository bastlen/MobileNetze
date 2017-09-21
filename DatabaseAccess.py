import sqlite3


# database Path
path = '/home/mone2/openbsc-0.14.0/openbsc/src/osmo-nitb/hlr.sqlite3'
# connect to DB
conn = sqlite3.connect(path)
#conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Subscriber")

out = cursor.fetchall()
strOut = ''
for x in out:
    print(x)

