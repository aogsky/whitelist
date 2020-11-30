import mysql.connector
import json

f = open('db-config.json')
s = f.read()
f.close()
config = json.loads(s)

mydb = mysql.connector.connect(
    host = config['host'],
    port = config['port'],
    database = config['database'],
    user = config['user'],
    password = config['password']
)

print(mydb)

mycursor = mydb.cursor()
print(mycursor)

#mycursor.execute("SHOW TABLES")
#print(mycursor)

#print(mycursor)

createtable = '''
CREATE TABLE iplist001
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip char(15) NOT NULL,
    count tinyint NOT NULL,
    status boolean NOT NULL
)'''
insertSQL = '''INSERT INTO iplist001 (ip, count, status) VALUES (%s, %s, %s)'''
#val = ("10.10.10.10", "1", "0")
def InsertData(IpList):
    for x in range(len(IpList)):
        val = (IpList[x], '1', '0')
        mycursor.execute(insertSQL, val)
    mydb.commit()

def printresult(cursor):
    for x in cursor:
        print(x)

#InsertData()
#mycursor.execute(createtable)
#mycursor.execute(insertSQL, val)
#mydb.commit()
#createtable()
#db.printresult(mycursor)

