import json
import mysql.connector


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

mycursor = mydb.cursor()

createtable = '''
CREATE TABLE {}
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip char(15) NOT NULL,
    count tinyint NOT NULL,
    status boolean NOT NULL
)'''

def insert_data(ip):
    sql = "INSERT INTO iplist001 (ip, count, status) VALUES (%s, %s, %s)"
    val = (ip, '1', '0')
    mycursor.execute(sql, val)
    mydb.commit()

def printresult(cursor):
    for x in cursor:
        print(x)

def query_status():
    print("What IP is:")
    ip = input()
    sql = "SELECT count,status FROM iplist001 WHERE ip='{}'"
    mycursor.execute(sql.format(ip))
    printresult(mycursor)
    print("Enter any key to continue...")
    input()

def update_count():
    print("What IP is:")
    ip = input()
    print("Update count to :")
    count = input()
    sql01 = "SELECT count FROM iplist001 WHERE ip='{}'"
    mycursor.execute(sql01.format(ip))
    _old_count = mycursor.fetchone()
    sql02 = "UPDATE iplist001 SET count = '{}' WHERE ip='{}'"
    mycursor.execute(sql02.format(count, ip))
    mydb.commit()
    result = "IP binded domain count was {}, now its {}"
    print(result.format(_old_count[0], count))
    print("Enter any key to continue...")
    input()