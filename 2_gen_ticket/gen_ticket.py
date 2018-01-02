import numpy as np,string
import MySQLdb
import redis

def gen_tickets(ticket_num,ticket_len):
    idx = np.random.randint(0,25,ticket_num * ticket_len)
    letters = np.array(list(string.ascii_uppercase))

#    print type(letters)
    s = letters[idx].tostring()

#    print s
    return [s[i*ticket_len : (i+1)*ticket_len] for i in range(ticket_num)]

#print gen_tickets(5,10)

def gen_a_ticket(len):
    idx = np.random.randint(0, 25, len)
    letters = np.array(list(string.ascii_uppercase))
    s = letters[idx].tostring()
    yield s



def insertMysql():
    db = MySQLdb.connect("127.0.0.1","root","1234","database_for_python")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS python_tickets")
    sql = """CREATE TABLE IF NOT EXISTS python_tickets(
                num INT,
                ticket_code CHAR(100))"""
    cursor.execute(sql)
    cursor.execute("INSERT INTO python_tickets VALUES('100','qqqwe')")
    db.commit()

    for i in range(1,201):
        ticket = gen_a_ticket(100).next()
        sql = "INSERT INTO python_tickets VALUES ('%d','%s')" % (i,ticket)
        cursor.execute(sql)
        db.commit()
    db.close()

def imsertRedis():
    rd = redis.Redis(host='127.0.0.1',port=6379,db=0)
    for i in range(1,201):
        ticket = gen_a_ticket(100).next()
        rd.set(i,ticket)
    rd.save()

    print rd.get(55)


if  __name__ == '__main__':
    #print gen_tickets(5,5)
    #insertMysql()
    imsertRedis()