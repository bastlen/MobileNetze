import sqlite3

# database Path
path = '/home/mone2/openbsc-0.14.0/openbsc/src/osmo-nitb/hlr.sqlite3'

# establish connection and return cursor obj
def connect():
    # connect to DB
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    return cursor

cursor = connect()

# get all Subscribers, return list
def getSubscribers():
    cursor.execute("SELECT * FROM Subscriber")
    outList = cursor.fetchall()
    return outList

#kllk
subscriberList = getSubscribers()
for x in subscriberList:
    print(x)